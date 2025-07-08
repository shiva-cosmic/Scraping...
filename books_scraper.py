'''
Libraries

pip install beautifulsoup4 html5lib requests



1.requests gets the web page.

2.BeautifulSoup4 reads and cleans the HTML.

3.html5lib helps parse it correctly.

--Parse--

Parse means to break down and understand something - usually data or text — in a structured way.

In web scraping:

To parse HTML means to read the HTML code of a web page and turn it into a format (like a tree) that your program can easily search, extract, or modify.


'''

import requests
from bs4 import BeautifulSoup

response = requests.get(url ='https://books.toscrape.com/')

# to check response use print(response) only if you want inside stuff then print(dir(response))

# Important if u want html content then use print(response.content)

# print(response.content)

page_source = (response.content)

# NOW if we want some specgific data from site then we use BeautifulSoup4

soup = BeautifulSoup(page_source)

print(dir(soup))