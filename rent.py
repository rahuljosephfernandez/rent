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

URL2 = 'https://www.leasebreak.com/advanced-search?asm%5BstartDate%5D=12%2F18%2F2020&asm%5BlengthStay%5D=6&asm%5BbIds%5D%5B1%5D=0&asm%5BnIds%5D%5B5%5D=0&asm%5BnIds%5D%5B6%5D=0&asm%5BnIds%5D%5B7%5D=0&asm%5BnIds%5D%5B8%5D=0&asm%5BnIds%5D%5B88%5D=0&asm%5BnIds%5D%5B10%5D=0&asm%5BnIds%5D%5B11%5D=0&asm%5BnIds%5D%5B13%5D=0&asm%5BnIds%5D%5B14%5D=0&asm%5BnIds%5D%5B12%5D=0&asm%5BnIds%5D%5B104%5D=0&asm%5BnIds%5D%5B15%5D=0&asm%5BnIds%5D%5B16%5D=0&asm%5BnIds%5D%5B136%5D=0&asm%5BnIds%5D%5B17%5D=0&asm%5BnIds%5D%5B71%5D=0&asm%5BnIds%5D%5B87%5D=0&asm%5BnIds%5D%5B87%5D=87&asm%5BnIds%5D%5B18%5D=0&asm%5BnIds%5D%5B18%5D=18&asm%5BnIds%5D%5B29%5D=0&asm%5BnIds%5D%5B31%5D=0&asm%5BnIds%5D%5B21%5D=0&asm%5BnIds%5D%5B1%5D=0&asm%5BnIds%5D%5B1%5D=1&asm%5BnIds%5D%5B3%5D=0&asm%5BnIds%5D%5B3%5D=3&asm%5BnIds%5D%5B30%5D=0&asm%5BnIds%5D%5B24%5D=0&asm%5BnIds%5D%5B2%5D=0&asm%5BnIds%5D%5B4%5D=0&asm%5BnIds%5D%5B100%5D=0&asm%5BnIds%5D%5B72%5D=0&asm%5BbIds%5D%5B2%5D=0&asm%5BnIds%5D%5B33%5D=0&asm%5BnIds%5D%5B84%5D=0&asm%5BnIds%5D%5B34%5D=0&asm%5BnIds%5D%5B73%5D=0&asm%5BnIds%5D%5B35%5D=0&asm%5BnIds%5D%5B85%5D=0&asm%5BnIds%5D%5B86%5D=0&asm%5BnIds%5D%5B36%5D=0&asm%5BnIds%5D%5B138%5D=0&asm%5BnIds%5D%5B37%5D=0&asm%5BnIds%5D%5B70%5D=0&asm%5BnIds%5D%5B39%5D=0&asm%5BnIds%5D%5B40%5D=0&asm%5BnIds%5D%5B41%5D=0&asm%5BnIds%5D%5B89%5D=0&asm%5BnIds%5D%5B42%5D=0&asm%5BnIds%5D%5B69%5D=0&asm%5BnIds%5D%5B43%5D=0&asm%5BnIds%5D%5B44%5D=0&asm%5BnIds%5D%5B91%5D=0&asm%5BnIds%5D%5B92%5D=0&asm%5BnIds%5D%5B93%5D=0&asm%5BnIds%5D%5B45%5D=0&asm%5BnIds%5D%5B95%5D=0&asm%5BnIds%5D%5B46%5D=0&asm%5BnIds%5D%5B96%5D=0&asm%5BnIds%5D%5B83%5D=0&asm%5BnIds%5D%5B74%5D=0&asm%5BnIds%5D%5B47%5D=0&asm%5BnIds%5D%5B67%5D=0&asm%5BnIds%5D%5B98%5D=0&asm%5BnIds%5D%5B101%5D=0&asm%5BnIds%5D%5B102%5D=0&asm%5BnIds%5D%5B103%5D=0&asm%5BnIds%5D%5B55%5D=0&asm%5BnIds%5D%5B48%5D=0&asm%5BnIds%5D%5B49%5D=0&asm%5BnIds%5D%5B99%5D=0&asm%5BnIds%5D%5B105%5D=0&asm%5BnIds%5D%5B50%5D=0&asm%5BnIds%5D%5B109%5D=0&asm%5BnIds%5D%5B51%5D=0&asm%5BnIds%5D%5B52%5D=0&asm%5BnIds%5D%5B53%5D=0&asm%5BnIds%5D%5B54%5D=0&asm%5BbIds%5D%5B3%5D=0&asm%5BnIds%5D%5B56%5D=0&asm%5BnIds%5D%5B63%5D=0&asm%5BnIds%5D%5B90%5D=0&asm%5BnIds%5D%5B64%5D=0&asm%5BnIds%5D%5B58%5D=0&asm%5BnIds%5D%5B68%5D=0&asm%5BnIds%5D%5B59%5D=0&asm%5BnIds%5D%5B97%5D=0&asm%5BnIds%5D%5B62%5D=0&asm%5BnIds%5D%5B57%5D=0&asm%5BnIds%5D%5B134%5D=0&asm%5BnIds%5D%5B26%5D=0&asm%5BnIds%5D%5B60%5D=0&asm%5BnIds%5D%5B107%5D=0&asm%5BnIds%5D%5B106%5D=0&asm%5BnIds%5D%5B94%5D=0&asm%5BnIds%5D%5B108%5D=0&asm%5BnIds%5D%5B61%5D=0&asm%5BnIds%5D%5B110%5D=0&asm%5BnIds%5D%5B111%5D=0&asm%5BnIds%5D%5B112%5D=0&asm%5BbIds%5D%5B4%5D=0&asm%5BnIds%5D%5B128%5D=0&asm%5BnIds%5D%5B131%5D=0&asm%5BnIds%5D%5B135%5D=0&asm%5BnIds%5D%5B120%5D=0&asm%5BnIds%5D%5B129%5D=0&asm%5BnIds%5D%5B122%5D=0&asm%5BnIds%5D%5B127%5D=0&asm%5BnIds%5D%5B117%5D=0&asm%5BnIds%5D%5B116%5D=0&asm%5BnIds%5D%5B125%5D=0&asm%5BnIds%5D%5B130%5D=0&asm%5BnIds%5D%5B132%5D=0&asm%5BnIds%5D%5B115%5D=0&asm%5BnIds%5D%5B66%5D=0&asm%5BnIds%5D%5B114%5D=0&asm%5BnIds%5D%5B126%5D=0&asm%5BnIds%5D%5B65%5D=0&asm%5BnIds%5D%5B119%5D=0&asm%5BnIds%5D%5B121%5D=0&asm%5BnIds%5D%5B118%5D=0&asm%5BnIds%5D%5B133%5D=0&asm%5BnIds%5D%5B124%5D=0&asm%5BbIds%5D%5B5%5D=0&asm%5BnIds%5D%5B28%5D=0&asm%5BbIds%5D%5B6%5D=0&asm%5BnIds%5D%5B137%5D=0&asm%5BnIds%5D%5B82%5D=0&asm%5BnIds%5D%5B81%5D=0&asm%5BnIds%5D%5B75%5D=0&asm%5BnIds%5D%5B76%5D=0&asm%5BnIds%5D%5B79%5D=0&asm%5BnIds%5D%5B80%5D=0&asm%5BnIds%5D%5B77%5D=0&asm%5BnIds%5D%5B113%5D=0&asm%5BnIds%5D%5B78%5D=0&asm%5Bprice%5D=0%3B1000000&asm%5BprivateRoom%5D=&asm%5BapartmentSizeId%5D=&asm%5BformType%5D=%22+.+AdvancedSearchModel%3A%3ACOLLAPSED_FORM_TYPE+.+%22&sortBy=&sortDirection='
page2 = requests.get(URL2)

soup2 = BeautifulSoup(page2.content, 'html.parser')

prices = soup2.find_all('span', class_='detail-right-price')

locations = soup2.find_all('span', class_='text')

def lbrent():

    print("LeaseBreak")

    print()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    print("Time: ", current_time, "Date: ", current_date)

    time.sleep(1.0)

    for price in prices:

        for location in locations:

            prc = price.text

            loc = location.text

        print(loc, prc)

        time.sleep(0.5)


uinput = str(input())

if uinput == "junehomes":

    jhrent()

elif uinput == "renthop":

    rhrent()

elif uinput == "leasebreak":

    lbrent()

else:

    print('invalid selection')