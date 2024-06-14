import pandas as pd
from bs4 import BeautifulSoup
import requests

#using the requests library, we will get the page we want to scrape and extract it’s HTML
f = requests.get('http://quotes.toscrape.com/')
#pass the site’s HTML text to BeautifulSoup, which will parse this raw data so it can be easily scraped:
soup = BeautifulSoup(f.text)
print(soup.get_text())

#in HTML file <span> class called text is highlighted. This is because you right-clicked on one of the quotes on the page, and all the quotes belong to this text class.
#We need to extract all the data in this class
for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("span",{"class":"text"})).text)

#We will use the find() and findAll() functions to extract all the author names within this tag.
for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("small",{"class":"author"})).text)

#the <meta> tag is wrapped by a parent <div> tag, with the class name tags.
#To extract all the tags on the page
for i in soup.findAll("div",{"class":"tags"}):
    print((i.find("meta"))['content'])

#create three empty arrays so we can store the data collected
quotes = []
authors = []
tags = []
for pages in range(1,10):   
    f = requests.get('http://quotes.toscrape.com/page/'+str(pages))
    soup = BeautifulSoup(f.text)    
    for i in soup.findAll("div",{"class":"quote"}):
        quotes.append((i.find("span",{"class":"text"})).text)  
   
    for j in soup.findAll("div",{"class":"quote"}):
        authors.append((j.find("small",{"class":"author"})).text)    
        for k in soup.findAll("div",{"class":"tags"}):
            tags.append((k.find("meta"))['content'])

#Finally, let’s consolidate all the data collected into a Pandas dataframe
finaldf = pd.DataFrame(
    {'Quotes':quotes,
     'Authors':authors,
     'Tags':tags
    })