from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urlopen(url, context = ctx).read()
tags = soup("span")
for tag in tags:
	print('Number:,'tag.get('span'),None)