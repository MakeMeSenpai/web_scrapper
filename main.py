"""Runs our basic webscapper"""
import requests
import re
from bs4 import BeautifulSoup as bs
print("*******************************")

# Load the webpage content
r = requests.get("https://champagneproxy.github.io/webscraping/example.html")
print("request uses GET method to collect our info")
print(r.content)
print("*******************************")

# Convert to a beautiful soup object
soup = bs(r.content, features="html.parser")

print("while soup makes it prettier")
# Pretty prints out our html
print(soup.prettify())
print("*******************************")

"""We can sort threw the data based on tags using BeautifulSoup find"""
print("we can search for certain tags")
# Finds first element tag matching str
first_header = soup.find("h2")
print(first_header)

# Finds all element tags matching str
headers = soup.find_all(["h1", "h2"]) # we can pass a list here too!
print(headers)
print("*******************************")

"""Sorting threw tags"""
print("Or search by attributes and nested elements")
# As well, we can look for certain attributes 
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)

# nested search
body = soup.find('body')

# From the body, we just want to grab from the first div
div = body.find('div')

# From the div, we want to grab the first header
header = div.find('h1')

print(header)
print("*******************************")

"""Using re, we can search for certain calls"""
print("Using re, we can search for certain calls")
# searches for only paragraphs with bolded text
bolded_paragraphs = soup.find_all("p", string=re.compile("bolded"))

print(bolded_paragraphs)

# searches for only h2 tags with the text of "header" but what about capital H?
# using (H|h) we are searching for <Header> and <header>
headers_re = soup.find_all("h2", string=re.compile("(H|h)eader"))
print(headers_re)
print("*******************************")

"""Simalure to css, we can use selectores to search items"""
print("Searching with selectors. Note: not all are supported")

content = soup.select("p")
print(content)

content = soup.select("div p")
print(content)

content = soup.select("h2 ~ p")
print(content)

bold_text = soup.select("p#paragraph-id b")
print(bold_text)
print("*******************************")

"""MORE!"""
print("and more!")
# We can use loops!
paragraphs = soup.select("body > p")

for paragraph in paragraphs:
	print(paragraph.select("i"))
print("*******************************")

# or search by certain styles
centered_stuff = soup.select("[align=middle]")
print(centered_stuff)
print("*******************************")

# We can parse collected information
header = soup.find("h2")
print(header) # <h2>First Header 2</h2>
print(header.string)  # First Header 2
print("*******************************")

# However if there are more than one element, we should use a method
div = soup.find("div")
print(div.string) # Not what you want, returns None
print(div.get_text())
print("*******************************")

# we can also get specific properties from an element
link = soup.find("a")
print(link['href'])
print("*******************************")

# And lastly follow down the path of tags
print(soup.body.div.h1.string)
print("*******************************")
