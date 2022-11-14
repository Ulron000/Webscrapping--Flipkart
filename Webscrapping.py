from bs4 import BeautifulSoup as bs
import requests
link=("https://www.flipkart.com/apple-iphone-13-pro-max-alpine-green-256-gb/p/itmd50ee574a9335?pid=MOBGC9VGH3SQEVZE&lid=LSTMOBGC9VGH3SQEVZEOQVWJR&marketplace=FLIPKART&q=iphone+13+pro+max&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_3_9_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_9_na_na_na&fm=Search&iid=6a88a702-251b-4ae2-ac46-b6f8707b1220.MOBGC9VGH3SQEVZE.SEARCH&ppt=sp&ppn=sp&ssid=6qv6wxd30w0000001668339303425&qH=5556902974bb931a")

page=requests.get(link)

page.content

soup=bs(page.content,"html.parser") 
soup

print(soup.prettify())

title=soup.title
title

print(title.string)

price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
print(price)

product_price=[]
for i in range(0,len(price)):
    product_price.append(price[i].get_text())
product_price

names=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
names

cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name

comment=soup.find_all("p",class_="_2-N8zT")
comment

cust_comment=[]
for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())
cust_comment

star=soup.find_all("div",class_="_3LWZlK _1BLPMq")
star

cust_stars=[]
for i in range(0,len(star)):
    cust_stars.append(star[i].get_text())
cust_stars

review=soup.find_all("div",class_="t-ZTKy")
review

cust_review=[]
for i in range(0,len(review)):
    cust_review.append(review[i].get_text())
cust_review

dateofbuyingprod=soup.find_all("p",class_="_2sc7ZR")
dateofbuyingprod

cust_dateofbuyingprod=[]
for i in range(0,len(dateofbuyingprod)):
    cust_dateofbuyingprod.append(dateofbuyingprod[i].get_text())
cust_dateofbuyingprod

import pandas as pd

df=pd.DataFrame()
df["Customer_Names"]=cust_name
df["Comments"]=cust_comment
df["Stars"]=cust_stars
df["Review"]=cust_review

df
