import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import os



save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

pw_url = "https://www.youtube.com/@PW-Foundation/videos"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36 Edg/101.0.1210.47"}
response = requests.get(pw_url,headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.find_all("a"))