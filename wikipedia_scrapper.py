import requests
from bs4 import BeautifulSoup

def scrapeWikiArticle(url):
	response = requests.get(url=url,)
	soup = BeautifulSoup(response.content, 'html.parser')
	
	allLinks = soup.find(id="mw-content-text").find_all("a")
	
	for link in allLinks:
		if link['href'].find("/wiki/") == -1:
			print(link)
		else:
			break
	

scrapeWikiArticle("https://en.wikipedia.org/wiki/Template:US_Army_navbox")
