import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the correct table
table = soup.find_all('table')[1]

# Get table headers
top_titles = table.find_all('th')
top_table_titles = [titles.text.strip() for titles in top_titles[1:]]  # Start from 1 to skip the first column

# Create an empty DataFrame with correct headers
df = pd.DataFrame(columns=top_table_titles)

# Iterate through the table rows
table_rows = table.find_all('tr')
for row in table_rows[1:]:  # Skip the header row
    td_data = row.find_all('td')
    temp_data = []

    for i in range(1, len(td_data)):  # Start from 1 to skip the first column
        temp = td_data[i].text.strip()
        temp = temp.replace(',', '').replace('+', '').replace('\n', '')
        temp_data.append(temp)

    # Check if the number of columns matches
    if len(temp_data) == len(top_table_titles):
        df.loc[len(df)] = temp_data  # Append the data as a new row

# Data Cleaning and Transformation
df.replace({'': None, 'N/A': None, '-': None}, inplace=True)

# # Convert relevant columns to numeric (if possible)
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
df[df.columns[0]] = df[df.columns[0]].astype(str)

# # Display the transformed data
print(df.head())
df = df.to_csv(r'C:\Users\Admin\Documents\Coronovires\COVID-19_data.csv', index=False)
