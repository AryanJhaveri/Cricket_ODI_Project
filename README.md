# Cricket_ODI_Project

## Overview

This project aims to explore the evolution of One Day International cricket matches' pace. We've analyzed data from over 4686 ODI matches, leveraging a custom Python script to scrape data from ESPN Cricinfo.

For more in-depth insights and discussions related to this project, check out my blog post:
- [My Project Blog](https://medium.com/@aryanjhaveri.aj/how-fast-has-the-game-of-cricket-become-the-numbers-b642affcb98c)
  
## Table of Contents
- [Webscrapping](#webscrapping)
- [Data Cleaning](#data-cleaning)
- [Data Analysis and Reporting](#data-analysis-and-reporting)
- [Predictive Modeling](#predictive-modeling)

## Webscrapping
- **Tools Used:** Selenium and BeautifulSoup for scraping ESPN Cricinfo.
- **Method:** Iterative scraping over multiple pages, extracting data into Pandas DataFrames.
- **Repository Contents:** [Webscrapping script](ESPNCricinfo_Webscrapping.py) and [Dataset](final_ODI_data.csv).

## Data Cleaning
- **Process:** Addressed missing values, optimized data types, and cleaned text data.
- **Enhancements:** Transformation of date formats and introduction of new columns for context.
- **Repository Contents:** [Data Cleaning](cricket_ODI_data_cleaning.ipynb).

## Data Analysis and Reporting
- **Approach:** In-depth analysis to derive insights on the changing pace of cricket.
- **Tools:** Power BI for creating dashboards and graphs.
- **Outputs:** [PowerBI Reports](ODI_PowerBI_dashboards.pdf).

## Predictive Modeling
- **Model:** Linear regression to predict future trends in cricket statistics.
- **Variables:** 'Balls Faced,' 'Strike Rate,' and 'Number of Matches.'
- **Purpose:** To forecast 4s, 6s, and Runs for the upcoming five years.
- **Repository Contents:**[Prediction Model](cricket_ODI_analysis_prediction.ipynb).

