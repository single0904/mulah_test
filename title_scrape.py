import requests

from bs4 import BeautifulSoup
import pandas as pd
import time
import streamlit as st

url = "https://www.theverge.com/archives/1"

response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
print(soup.prettify())
articles = []
count = 0

for row in soup.select('div.duet--layout--river div.mx-auto'):
    count += 1
    title1 = row.find('div', class_ = 'duet--content-cards--content-card').find('div', class_ = 'flex min-w-0 flex-1 flex-col').find('div', class_ = 'font-polysans text-black dark:text-gray-ef leading-130').find('div', class_ = 'inline').get_text()
    # title2 = row.find('div', class_ = 'duet--content-cards--content-card').find('div', class_ = 'flex items-center').find('div', 'max-w-content-block-mobile sm:w-content-block-standard sm:max-w-content-block-standard').find('h2', class_ = 'font-polysans text-20 font-bold leading-100 tracking-1 md:text-24').find('a').get_text()
    url1 = row.find('div', class_ = 'duet--content-cards--content-card').find('a', class_ = 'hover:shadow-underline-inherit after:absolute after:inset-0').get('href')
    articles.append([title1, url1])
    # articles.append([title2])
print(articles)

st.write(articles)


