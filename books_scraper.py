'''
Libraries

pip install beautifulsoup4 html5lib requests



1.requests gets the web page.

2.BeautifulSoup4 reads and cleans the HTML.

3.html5lib helps parse it correctly.

4.import csv

--Parse--

Parse means to break down and understand something - usually data or text — in a structured way.

In web scraping:

To parse HTML means to read the HTML code of a web page and turn it into a format (like a tree) that your program can easily search, extract, or modify.


'''

import requests
from bs4 import BeautifulSoup
import csv

response = requests.get(url ='https://books.toscrape.com/')

# to check response use print(response) only if you want inside stuff then print(dir(response))

# Important if u want html content then use print(response.content)

# print(response.content)

page_source = (response.content)

# NOW if we want some specgific data from site then we use BeautifulSoup4

soup = BeautifulSoup(page_source, 'html.parser')

# print(dir(soup))

# print(soup)

# for one, and it will return first p of whole html

# print(soup.find('p'))

# for all (you can use any ex: p, h1, li, ol, header, footer anyone u just have to target that element of which u required data )

# print(soup.find_all("p"))


# now if you want to scrape the Prize and product name as well as product link then you have to do this and this is the main thing in scraping data.


heading_elements = (soup.find_all('h3'))
# to get the price of prduct, u can target class as well as id
pricing_elements = soup.find_all('p', {'class': 'price_color'})

complete_data = []
for each_heading, each_pricing_element in zip(heading_elements, pricing_elements):
  book_name = (each_heading.get_text())
# to get links of the product
  each_link = each_heading.find("a")
  book_link = (each_link.get('href'))

  book_price = (each_pricing_element.get_text())

  complete_data.append({'book_name': book_name, 'book_price': book_price, 'book_link' : book_link })

csv_filename = 'scraped_book.csv'
fieldNames = [ 'book_name', 'book_price', 'book_link']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
  csv.DictWriter(csv_file, fieldnames=fieldNames).writerows(complete_data)