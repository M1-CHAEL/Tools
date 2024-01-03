import requests
from bs4 import BeautifulSoup

def scrapeWikiArticle(url):
	response = requests.get(url=url,)
	soup = BeautifulSoup(response.content, 'html.parser')
	
	allLinks = soup.find(id="bodyContent").find_all("a")
	linkToScrape = 0
	
	for link in allLinks:
		if link['href'].find("/wiki/") == -1:
			continue
		linkToScrape = link
		break
	print("http://en.wikipedia.com" + link['href'])
	
#use below scrapper function on not protected wikis, i.e. not military wikis as you will be blocked :(
#for more information https://en.wikipedia.org/wiki/Wikipedia:Protection_policy
#scrapeWikiArticle("https://en.wikipedia.org/wiki/Template:US_Army_navbox")
