import requests 
# import pandas as pd
import base64
from bs4 import BeautifulSoup
import re


# URL = http://free-proxy.cz/en/proxylist/country/all/all/ping/all?do=searchFilter-submit
# POST REQUEST
with open("htdump.html") as file:
	data = file.readlines()
PATTERN = "document.write(Base64.decode(\"MTc4LjIxMy4xNDUuMjQ=\"))"

for linerow, row in enumerate(data):
	if "Base64" in row:
		str_port = (data[linerow + 5]).strip()
		lookbehind = "(?<=document.write\(Base64.decode\(\")"
		lookahead = "(?=\"\)\))"
		rr = re.findall(f"{lookbehind}.+{lookahead}", row)
		try:
			b64string = rr[0]
			url_encoded = base64.b64decode(b64string)
			url_decoded = url_encoded.decode("utf-8")
			print(f"{b64string} => {url_decoded}:{str_port}")
		except IndexError:
			continue
