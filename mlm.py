import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.s4ds.com/es/blog/mejores-empresas-de-venta-directa-y-multinivel/"
response = requests.get(url)

response.status_code
soup= BeautifulSoup(response.text)

#soup.find_all("h2")
#soup.find("tbody")
#soup.find_all("tr")[1].find("a").text

lml = soup.find_all("tr")

compania = [ x.find_all("td")[1].text for x in lml]
value = [ x.find_all("td")[-1].text for x in lml]
rank = [x.find("td").text for x in lml]

datalml = pd.DataFrame({
    'rank':rank,
    'compania':compania,
    'value':value})
datalml