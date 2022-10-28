import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='/Users/deanarriviello/Documents/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.nfl.com/stats/team-stats/')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('div', attrs={"class": "d3-o-club-fullname"}):
    name = a
    results.append(name.text)
print(results)

df = pd.DataFrame({'Names': results})
df.to_csv('team_names.csv', index=False, encoding='utf-8')
# series1 = pd.Series(results, name='Names')
