# COVID-19 Data Scraper and Processor

This Python script scrapes the latest COVID-19 data from the Worldometers website, processes the data, and saves it as a CSV file for further analysis. The script is designed to extract useful information, clean the data, and store it in a structured format.

## Features

- **Web Scraping**: The script uses `requests` and `BeautifulSoup` to fetch and parse HTML data from Worldometers.
- **Data Cleaning**: The scraped data is cleaned and transformed to ensure consistency and accuracy.
- **Data Export**: The processed data is exported to a CSV file for easy access and further analysis.

## Requirements

To run this script, you need to have Python installed along with the following packages:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install these packages using `pip`:

```
pip install requests beautifulsoup4 pandas

````

Script Details
--------------

### 1\. Web Scraping

The script fetches COVID-19 data from the [Worldometers website](https://www.worldometers.info/coronavirus/). It targets the table that contains global COVID-19 statistics.

### 2\. Data Cleaning and Transformation

*   **Header Extraction**: The script extracts the column headers from the table.
*   **Row Iteration**: It iterates through each row of the table, extracting and cleaning the data.
*   **Data Cleaning**: The data is cleaned by removing unwanted characters (like commas and plus signs) and converting columns to appropriate data types.
*   **Handling Missing Values**: Missing values are replaced with `0` where necessary.

### 3\. Data Export

After processing, the cleaned data is saved as a CSV file at the specified path: 

Usage
-----

1.  **Run the Script**: Execute the script in your Python environment.

```
python covid_data_scraper.py
```

2.  **View the Output**: The output CSV file will be saved in the specified directory. Open it with any CSV viewer or spreadsheet software like Excel.



Customization
-------------

You can customize the script to save the output CSV file to a different location by modifying the file path in the script:

```python
df.to_csv(r'path_to_your_directory\COVID-19_data.csv', index=False)
```
