from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl 
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
nums = []
for tag in tags:
	nums.append(int((tag.contents[0])))
print("Count " + str(len(nums)))
print("Sum " + str(sum(nums)))
	
