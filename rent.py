from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time
import os

URL0 = 'https://junehomes.com/residences/new-york-city-ny/upper-east-side?movein=2020-12-18&moveout=2021-06-18'
page0 = requests.get(URL0)

soup0 = BeautifulSoup(page0.content, 'html.parser')

def jhrent():

    print("June Homes")

    print()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    print("Time: ", current_time, "Date: ", current_date)

    time.sleep(1.0)

    info = soup0.find_all(class_="HomeCard_topInfo__3jvfo")

    for inf in info:

        prc = inf.find(class_="HomeCard_priceValue__3RGAX")

        typ = inf.find(class_="HomeCard_info__3uea0")

        print(typ.text, prc.text)

        time.sleep(0.5)

URL1 = 'https://www.renthop.com/search/nyc?min_price=0&max_price=15000&no_fee=on&features%5B%5D=Sublet&q=&neighborhoods_str=49%2C29%2C30&sort=hopscore&page=1&search=1'
page1 = requests.get(URL1)

soup1 = BeautifulSoup(page1.content, 'html.parser')

def rhrent():

    print("RentHop")

    print()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    print("Time: ", current_time, "Date: ", current_date)

    time.sleep(1.0)

    prc = soup1.find_all(class_="d-inline-block align-bottom")

    for p in prc:

        pr = p.text

        print(pr)

        time.sleep(0.5)

uinput = str(input())

if uinput == "junehomes":

    jhrent()

elif uinput == "renthop":

    rhrent()

else:

    print('invalid selection')