import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://realpython.github.io/fake-jobs/'

response = requests.get(URL, timeout=10)

html = response.text

soup = BeautifulSoup(html, 'html.parser')
results = soup.find(id='ResultsContainer')
# job_cards = results.find_all('div', class_='card-content')
job_title = results.select('#ResultsContainer h2.title, h3, p.location')
for i in job_title:
    print(i.get_text())