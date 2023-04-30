import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.searchenginejournal.com/tiktok-shop-social-commerce/485576/'

# Send GET request and parse HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags in the HTML content
anchor_tags = soup.find_all('a')

# Extract anchor text and href attributes from each anchor tag
for anchor_tag in anchor_tags:
    anchor_text = anchor_tag.text.strip()
    href = anchor_tag.get('href')
    print(f'{anchor_text}: {href}')
