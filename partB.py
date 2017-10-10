import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
x = 0
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
print("Retriving: " + url)
while x < count:
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	num = []
	tags = soup("a")
	for tag in tags:
		num.append(tag.get('href', None))
	url = num[pos-1]
	print("Retrieving: " + url)
	x+=1


