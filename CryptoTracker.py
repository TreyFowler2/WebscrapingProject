from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

url = 'https://cryptoslate.com/highest-volume/'

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber= '+12058963685'
myCellphone = '+12513480758'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)
print()

tablerows = soup.findAll("tr")

for row in tablerows[1:6]:
    td = row.findAll("td")
    name = td[1].text.strip()
    price = td[2].text.strip()
    tfhourchange = td[3].text

    print(f'Name & Ticker: {name}')
    print(f'Current Price: {price}')
    print(f'24 Hour Change: {tfhourchange}')
    print()

####################################################

for row in tablerows[1:500]:
    td = row.findAll("td")
    name = td[1].text.strip()
    price = td[2].text.strip()

    if name == "Bitcoin BTC":
        price = price.replace('$','')
        price = price.replace(',','')
        if float(price) < 40000:
            textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber, body="Bitcoin is under $40,000")
            print(textmsg.status)

    if name == "Ethereum ETH":
        price = price.replace('$','')
        price = price.replace(',','')
        if float(price) < 3000:
            textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber, body="Ethereum is under $3,000")
            print(textmsg.status)
