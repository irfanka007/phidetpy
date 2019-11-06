#Retrieving page ranking
import requests 
from bs4 import BeautifulSoup 
import csv 
import re

a=input("enter the url:")
b = "https://www.alexa.com/siteinfo/"
URL=b+a
#print(URL)
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib')
k=soup.prettify()
#print(a) 

table = soup.find('div', attrs = {'class':'rank-global'}) 
if table==None:
    print("suspecious url ")
else:
    for row in table.findAll('p', attrs = {'class':'big data'}):
        g=row.text
    temp = re.findall(r'\d+', g) 
    for i in temp:
        val=int(i)
        #print(type(val))
    print("website rank of ",a," is ",val)
    print("URL seems legitimate")


    
