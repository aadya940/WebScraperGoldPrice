''' Writing a python script to fetch Real-Time 22k Gold Price Data '''

import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.melorra.com/jewellery/gold-rate-ahmedabad/')
data = response.text

soup = BeautifulSoup(data, 'lxml')

tag = soup.find('div', class_='overflow-auto mt-5')
tag = tag.find_all('td')
print('Price of 1 gram 22k Gold is {}'.format(tag[1].text))

