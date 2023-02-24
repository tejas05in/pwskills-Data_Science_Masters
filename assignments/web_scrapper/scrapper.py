from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

edgeBrowser = webdriver.Edge("D:/pwskills-Data_Science_Masters/assignments/web_scrapper/msedgedriver.exe")
edgeBrowser.get("https://www.youtube.com/@PW-Foundation/videos")
edgeBrowser.execute_script("window.scrollTo(0,2000)")
time.sleep(1)
content = edgeBrowser.page_source.encode("utf-8").strip()
soup = BeautifulSoup(content,"html.parser")
edgeBrowser.close()

#print(soup)

videos =  soup.find_all("a",id="thumbnail")
video = []
for i in videos:
    try:
        s = "https://www.youtube.com/" + i['href']
        video.append(s)
    except:
        continue

thumbnails  = soup.find_all("img",{"class":"yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded"})
thumbs = []
for i in thumbnails:
    thumbs.append(i["src"])

titles = soup.find_all("yt-formatted-string",id="video-title")
title = []
for i in titles:
    title.append(i.text)

views = []
for i in range(0,len(soup.find_all("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"})),2):
    views.append(soup.find_all("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"})[i].text)

timeofposting = []
for i in range(1,len(soup.find_all("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"})),2):
    timeofposting.append(soup.find_all("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"})[i].text)

final = pd.DataFrame({"video_link": video[:5],"thumbnails": thumbs[:5],"titles" : title[:5],"views": views[:5],"time of posting": timeofposting[:5]})

print(final)