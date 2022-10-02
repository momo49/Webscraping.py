import requests
from bs4 import BeautifulSoup
#call request from the ask website
page = requests.get('https://www.metoffice.gov.uk/weather/forecast/gcqdt4b2x#?date=2022-09-03')
#makes web scraping easy for the classes, css and editing easier
soup =BeautifulSoup(page.content, 'html.parser')
#find for all the div
#print(soup.find_all('div'))
week = soup.find(id='2022-09-03')
#shows everything that is inside the div
print(week)

