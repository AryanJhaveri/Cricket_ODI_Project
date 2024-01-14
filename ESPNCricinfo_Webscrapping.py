# -*- coding: utf-8 -*-
#pip install selenium

#!apt-get update
#!apt install -y chromium-chromedriver

import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up ChromeDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up ChromeDriver executable path
chrome_options.add_argument('executable_path=/usr/lib/chromium-browser/chromedriver')

# Configure ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

def scrape_page(url):
    # Configure ChromeDriver options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except Exception as e:
        print(f"Error accessing page: {e}")
        soup = None
    finally:
        driver.quit()

    return soup

def scrape_all_pages(base_url, num_pages):
    dfs = []  # List to store DataFrames from each page

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}&page={page_num}"

        #print(f"Scraping page {page_num} with URL: {url}")
        # Attempt to scrape the page
        soup = scrape_page(url)

        # Check if the page was successfully scraped
        if soup is None:
            print(f"Failed to scrape page {page_num}. Skipping.")
            continue

        # Extract data from the table
        target_tables = soup.find_all('table', {'class': 'engineTable'})
        target_table = target_tables[2]

        # Check if the table is found
        if target_table is None:
            print(f"No table found on page {page_num}. Skipping.")
            continue

        headers = [th.text.strip() for th in target_table.find_all('th')]
        data_rows = []
        for tr in target_table.find_all('tr')[1:]:
            row = [td.text.strip() for td in tr.find_all('td')]
            data_rows.append(row)

        # Create DataFrame for the current page
        df = pd.DataFrame(data_rows, columns=headers)
        dfs.append(df)

    # Concatenate DataFrames from all pages into a single DataFrame
    final_df = pd.concat(dfs, ignore_index=True)

    return final_df

base_url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=start;size=200;template=results;type=batting;view=innings"
num_pages = 520

# Run the scraping function
result_df = scrape_all_pages(base_url, num_pages)

result_df

csv_data = result_df.to_csv(index=False)

# Save CSV data to a file
with open('output_file.csv', 'w') as csv_file:
    csv_file.write(csv_data)

# Download the CSV file
from google.colab import files
files.download('output_file.csv')

