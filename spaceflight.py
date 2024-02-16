#Import necessary libraries
import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# List of API Endpoints
api_urls = [
    "https://api.spaceflightnewsapi.net/v4/articles/?format=json",
     "https://api.spaceflightnewsapi.net/v4/blogs/?format=json",
     "https://api.spaceflightnewsapi.net/v4/info/?format=json",
     "https://api.spaceflightnewsapi.net/v4/reports/?format=json"
]

# Initialize an empty list to store data from all URLs
all_data = []

# Iterate over each API URL
for idx, api_url in enumerate(api_urls):
    print(f"Processing API URL {idx+1}/{len(api_urls)}: {api_url}")
    
    # Make the GET request
    response = requests.get(api_url)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        print(response.json())
    else:
        print("Error fetching data. Status code:", response.status_code)
        continue  # Move to the next URL if there's an error
    
    # Append data to the list
    all_data.extend(data)

# Convert combined data to Pandas DataFrame
combined_df = pd.DataFrame(all_data)

# Save DataFrame as Parquet file
pq.write_table(pa.Table.from_pandas(combined_df), 'spaceflightnews_combined_articles.parquet')
#print Parquet file
print("Combined spaceflightnews articles data saved to spaceflightnews_combined_articles.parquet")
