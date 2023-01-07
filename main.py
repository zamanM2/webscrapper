import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path='/Users/macbook/Desktop/SamsungCloud/chromedriver.exe')

driver = webdriver.Chrome(service=driver_service)
driver.get('https://oxylabs.io/blog')
results = []
other_results = []

content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='blog-card__content-wrapper'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
for a in soup.findAll(attrs='css-1kfmdo4 emlf3670'):
    name = a.find('p')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1kfmdo4 emlf3670'):
    head = b.find('h5')
    if head not in results:
        other_results.append(head.text)

df = pd.DataFrame({'Name': results, 'Head': other_results})
df.to_csv('name.csv', index=False, encoding='utf-8')

