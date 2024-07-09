# Spaceflight News ETL

This repository contains a simple ETL pipeline for fetching data from the Spaceflight News API, processing it, and storing it in a Parquet file format.

## Repository Contents

- `spaceflight.py`: Python script to fetch and process data from the Spaceflight News API.
- `spaceflightnews_combined_articles.parquet`: Parquet file containing the combined data fetched from the API.

## Cloning the Repository

To clone this repository, use the following command:

```sh
git clone https://github.com/MalshaDissanayake/spaceflightnews-el.git
```

## Dependencies

The script requires the following Python libraries:

- `requests`
- `pandas`
- `pyarrow`

You can install these dependencies using `pip`:
```sh
    pip install requests pandas pyarrow
```
## Usage

1. Ensure all dependencies are installed.
2. Run the `spaceflight.py` script to fetch and process the data:
```sh
    python spaceflight.py
```
3. The script will fetch data from the following API endpoints:
    - Articles: `https://api.spaceflightnewsapi.net/v4/articles/?format=json`
    - Blogs: `https://api.spaceflightnewsapi.net/v4/blogs/?format=json`
    - Info: `https://api.spaceflightnewsapi.net/v4/info/?format=json`
    - Reports: `https://api.spaceflightnewsapi.net/v4/reports/?format=json`

4. The fetched data will be combined into a single Pandas DataFrame and saved as a Parquet file named `spaceflightnews_combined_articles.parquet`.

## Script Details

The `spaceflight.py` script performs the following steps:

1. Imports necessary libraries.
2. Defines a list of API endpoints to fetch data from.
3. Initializes an empty list to store data from all endpoints.
4. Iterates over each API URL, makes a GET request, and checks for a successful response.
5. Appends the fetched data to the list.
6. Converts the combined data into a Pandas DataFrame.
7. Saves the DataFrame as a Parquet file named `spaceflightnews_combined_articles.parquet`.
8. Prints a success message upon completion.

## Example Output

The combined data will be saved in the `spaceflightnews_combined_articles.parquet` file, which can be read using libraries like `pandas` and `pyarrow` for further analysis.
```sh
    import pandas as pd

    # Read the Parquet file
    df = pd.read_parquet('spaceflightnews_combined_articles.parquet')

    # Display the DataFrame
    print(df.head())
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
