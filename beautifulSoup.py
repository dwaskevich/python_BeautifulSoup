import requests
from bs4 import BeautifulSoup

url = 'https://github.com/dwaskevich?tab=repositories'

# Send a GET request to URL
response = requests.get(url)

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

numRepos = 0

for tag in soup.find_all('a', {'itemprop': 'name codeRepository'}):
    print(tag.string, tag.get('href'))
    numRepos += 1

print(f'Number of repositories found = {numRepos}')

