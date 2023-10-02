import re

import online
import requests
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename

import TarcRepo
class HtmlParse:
    def __init__(self, soup):
        self.soup = soup

    def find_tags_with_class(self, tag, className):
        outputLst = []
        for t in self.soup.find_all(tag, {"class": className}):
            outputLst.append(t)
        return outputLst


username = input()
password = input()
searchTerm = input()

# login then search
r = TarcRepo.TarcRepo()
r.repo_login("2201610", "TJS-12345")
url = (r.repo_search("AACS3064"))

# online.start()

# initialise requests cookies
session = requests.session()
for cookie in r.driver.get_cookies():
    session.cookies.set(cookie['name'], cookie['value'])

page = requests.get(r.driver.current_url).text
soup = BeautifulSoup(page, 'html.parser')
parse = HtmlParse(soup)

searchResultLinks = []
for a in parse.find_tags_with_class("tr", "ep_search_result"):
    searchResultLinks.append(a.a.get('href'))

PDFLinkName = []
for link in searchResultLinks:
    pdfLink = ""
    pdfName = ""

    soup = BeautifulSoup(requests.get(link).text, 'html.parser')
    for name in soup.find_all("h1", {"class": "ep_tm_pagetitle"}):
        pdfName = (re.sub('\s+', ' ', name.text).strip())
    for a in soup.find_all("a", {"class": "ep_document_link"}):
        pdfLink = (a.get('href'))

    if pdfLink is not None and pdfName is not None:
        PDFLinkName.append((pdfLink, pdfName))
    else:
        print("Invalid Links in " + pdfLink if pdfLink is not None else "" + pdfName if pdfName is not None else "")

# download file
for linkNameTuple in PDFLinkName:
    pdfResponse = session.get(linkNameTuple[0])
    cleanFileName = sanitize_filename(linkNameTuple[1], platform="Windows",replacement_text="-")

    # write bytes from webpage downloaded into a file in download path
    with open(r.downloadPath + "\\" + cleanFileName + ".pdf", 'wb') as f:
        f.write(pdfResponse.content)

    print(cleanFileName + " downloaded")

r.driver.close()
