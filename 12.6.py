# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'https://py4e-data.dr-chuck.net/comments_42.html'
# url = 'http://www.dr-chuck.com/page1.htm'
url = "https://py4e-data.dr-chuck.net/comments_2135785.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# TAG: <span class="comments">2</span>
# tag.contents[0] gives numbers like the "2" above
# Retrieve all of the anchor tags
tags = soup('span')

sum = 0
for tag in tags:
    # Look at the parts of a tag
    value = int(tag.contents[0])
    sum = sum + value
print("SUM", sum)