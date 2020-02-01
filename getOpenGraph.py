# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import re


def getOpenGraph(url):
    soup = BeautifulSoup(requests.get(url).content.decode(
        'utf-8', 'ignore'), 'html.parser')
    data = {}
    for item in soup.find_all("meta", {"property": re.compile("og:.*?")}):
        data[item["property"][3:]] = item["content"]
    return data
