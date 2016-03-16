#the first verison, can do larger depth by adding more layers
import os
import requests
from bs4 import BeautifulSoup
import HTMLParser
import time
from random import randint
import sys
import re
import string
import socket
import cookielib
os.environ['http_proxy']=''
jar=cookielib.CookieJar()

#add headers
# ex: headers = {xxxxx}

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)
dic={}
#add links
#links=['']
link=links[0]
total_links=""
total_attributes=""
res = requests.get(link, headers=headers, cookies=jar)
soup = BeautifulSoup(res.text)
#add attribute
#attribute_table = soup.findAll('attribute')
total_attributes=remove_tags(str(attribute_table[0])).strip()
# add sleep
total_links_list = open('crawker.txt','w')
for l in soup.findAll('a',{'href':True}):
    if link not in dic:
        dic[link]=1
        print str(link) + ',' + str(total_attributes)
        total_links_list.write(str(link) + ',' + str(total_attributes) + "\n")
    total_links=l
    for ee in re.findall('''href=["'](.[^"']+)["']''', str(total_links), re.I):
        if ee[0:4]=="http":
            link=ee
        elif  ee[0:2]=="//":
            link="http:"+ee
        elif len(ee)!=0 and ee[0]=="/":
            link=links[0][0:len(links[0])-1]+ee
        elif ee[0]!="/" and ee[0]!="/":
            link=links[0][0:len(links[0])-1]+"/"+ee
    res=requests.get(link, headers=headers, cookies=jar)
    soup=BeautifulSoup(res.text)
    attribute_table = soup.findAll('attribute')
    if len(attribute_table)!=0:
        total_attributes=remove_tags(str(attribute_table[0])).strip()
    else:
        total_attributes=""
    # add sleep
total_links_list.close()
