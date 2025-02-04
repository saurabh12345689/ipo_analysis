import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Directory for storing master files
MASTER_DIR = 'master_files'

# Ensure the directory exists
os.makedirs(MASTER_DIR, exist_ok=True)

def fetch_ipo_data(url):
    # Send a GET request to fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the IPO name from the webpage title or header
    ipo_name = soup.find('h1').text.strip().split('IPO')[0].strip()

    # Find all tables with the 'table' class
    tables = soup.find_all('table', class_='table')

    for idx, table in enumerate(tables):
        rows = table.find_all('tr')

        # Extract headers
        headers = [header.text.strip() for header in rows[0].find_all('th')]
        if not headers:
            # Assign default column names if no headers are found
            headers = [f"Column_{i+1}" for i in range(len(rows[0].find_all('td')))]

        # Extract table data
        table_data = []
        for row in rows:
            columns = row.find_all('td')
            if columns:
                row_data = [col.text.strip() for col in columns]
                table_data.append(row_data)

        # Create a DataFrame
        df = pd.DataFrame(table_data, columns=headers)
        df['IPO Name'] = ipo_name  # Add IPO Name column

        # Determine the master file path
        master_file = os.path.join(MASTER_DIR, f'Ipo_master_table_{idx+1}.csv')

        if os.path.exists(master_file):
            # Load the master file
            master_df = pd.read_csv(master_file)

            # Align headers by filling missing columns
            all_columns = set(master_df.columns).union(df.columns)
            master_df = master_df.reindex(columns=all_columns, fill_value='N/A')
            df = df.reindex(columns=all_columns, fill_value='N/A')

            # Append the data
            combined_df = pd.concat([master_df, df], ignore_index=True)
        else:
            # If master file doesn't exist, use the df as the master data
            combined_df = df

        # Save the updated master file
        combined_df.to_csv(master_file, index=False)
        print(f"Updated master file: {master_file}")

def main():
    # List of URLs to process
    urls = [
        'https://www.chittorgarh.com/ipo/senores-pharmaceuticals-ipo/1943/'
        # 'https://www.chittorgarh.com/ipo/unimech-aerospace-ipo/1942/'
        # 'https://www.chittorgarh.com/ipo/carraro-india-ipo/1945/'
        # 'https://www.chittorgarh.com/ipo/ventive-hospitality-ipo/1939/'
        # 'https://www.chittorgarh.com/ipo/concord-enviro-ipo/1941/'
        # 'https://www.chittorgarh.com/ipo/transrail-lighting-ipo/1933/'
        # 'https://www.chittorgarh.com/ipo/dam-capital-advisors-ipo/1936/'
        # 'https://www.chittorgarh.com/ipo/sanathan-textiles-ipo/1940/'
        # 'https://www.chittorgarh.com/ipo/mamata-machinery-ipo/1937/'
        # 'https://www.chittorgarh.com/ipo/international-gemmological-institute-ipo/1930/'
        # 'https://www.chittorgarh.com/ipo/inventurus-knowledge-solutions-ipo/1926/'
        # 'https://www.chittorgarh.com/ipo/mobikwik-ipo/1928/'
        # 'https://www.chittorgarh.com/ipo/sai-life-sciences-ipo/1925/'
        # 'https://www.chittorgarh.com/ipo/vishal-mega-mart-ipo/1924/'
        # 'https://www.chittorgarh.com/ipo/property-share-reit-ipo/1917/'
        # 'https://www.chittorgarh.com/ipo/suraksha-diagnostic-ipo/1918/'
        # 'https://www.chittorgarh.com/ipo/ntpc-green-energy-ipo/1902/'
        # 'https://www.chittorgarh.com/ipo/blackbuck-ipo/1904/'
        # 'https://www.chittorgarh.com/ipo/niva-bupa-health-insurance-ipo/1899/'
        # 'https://www.chittorgarh.com/ipo/swiggy-ipo/1896/'
        # 'https://www.chittorgarh.com/ipo/sagility-india-ipo/1898/'
        # 'https://www.chittorgarh.com/ipo/afcons-infrastructure-ipo/1881/'
        # 'https://www.chittorgarh.com/ipo/waaree-energies-ipo/1888/'
        # 'https://www.chittorgarh.com/ipo/deepak-builders-engineers-ipo/1890/'
        # 'https://www.chittorgarh.com/ipo/hyundai-motor-ipo/1879/'
        # 'https://www.chittorgarh.com/ipo/garuda-construction-and-engineering-ipo/1883/'
        # 'https://www.chittorgarh.com/ipo/diffusion-engineers-ipo/1874/'
        # 'https://www.chittorgarh.com/ipo/krn-heat-exchanger-ipo/1864/'
        # 'https://www.chittorgarh.com/ipo/manba-finance-ipo/1866/'
        # 'https://www.chittorgarh.com/ipo/western-carriers-india-ipo/1844/'


    ]

    # Step 1: Fetch and save IPO data, directly appending to master files
    for url in urls:
        print(f"Processing URL: {url}")
        fetch_ipo_data(url)

if __name__ == '__main__':
    main()
