# python_BeautifulSoup
HTML parsing with BeautifulSoup 4

Simple Python script to list github repositories (and their url's) in the console window.

Console input requests a github user name. Response method in requests package returns web page html.

BeautifulSoup html parser is used to locate the 'a' tags associated with repositories (data-tab-item attribute = repositories) and build a url link to the user's repositories page (href.

Another html request is issued with the extracted repo url and BeautifulSoup is again used to locate 'a' tags with repository names (itemprop attribute = name codeRepository) and url's (href).

Finally, repository names and clickable url's are output to the console.
