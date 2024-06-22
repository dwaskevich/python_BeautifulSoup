import requests
from bs4 import BeautifulSoup

baseURL = 'https://github.com/'  # Github domain

# get user input
while True:
    url = input("Enter Github user name: ")

    url = baseURL + url  # generate full url
    print(url)

    # Send a GET request to the full/generated url (i.e. user's github landing page)
    response = requests.get(url)

    # check for server response
    if response.status_code == requests.codes.ok:
        break
    else:
        print('No response from ' + url)

# process server response
html_doc = response.text  # extract html contents
soup = BeautifulSoup(html_doc, 'html.parser')  # use BeautifulSoup to parse html

# variable to hold repo url
repoURL = ''

# find repo page url
for tag in soup.find_all('a', {'data-tab-item': 'repositories'}):
    repoURL = tag.get('href')

# construct repositories url (remove trailing '/' on base URL to avoid double slash)
url = baseURL.removesuffix('/') + repoURL

print('Repositories url link: ', url)  # put link in console

# Send a GET request to repositories url
response = requests.get(url)

html_doc = response.text  # extract html contents
soup = BeautifulSoup(html_doc, 'html.parser')  # use BeautifulSoup to parse html

numRepos = 0  # variable to count number of repositories

# find all public repositories, print names and url's
for tag in soup.find_all('a', {'itemprop': 'name codeRepository'}):
    print(tag.string, baseURL.removesuffix('/') + tag.get('href'))
    numRepos += 1

print(f'Number of repositories found = {numRepos}')
