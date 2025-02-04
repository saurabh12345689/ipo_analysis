import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://www.chittorgarh.com/ipo/unimech-aerospace-ipo/1942/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all the text content from the page
    page_content = soup.get_text(strip=True)
    
    # Create a DataFrame to store the extracted content
    data = {'Content': [page_content]}
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('ipo_page_content.csv', index=False)
    print("Content extracted and saved to ipo_page_content.csv")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
