import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/')

soup = BeautifulSoup(html, 'html.parser')

tempMin = soup.find(id='min-temp-1')
print(tempMin.text)