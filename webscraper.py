import requests 
from bs4 import BeautifulSoup as bs
import sys
sys.setrecursionlimit(30000)

# check whether the image is an icon 
def isIcon(pic):

	if pic == 'orphotdir/scent.jpg':
		return True
	elif pic == 'orphotdir/sun.jpg':
		return True
	elif pic == 'orphotdir/tempcool.jpg':
		return True
	elif pic == 'orphotdir/tempcold.jpg':
		return True
	elif pic == 'orphotdir/summer.jpg':
		return True
	elif pic == 'orphotdir/paper.jpg':
		return True
	elif pic == 'orphotdir/deepshade.jpg':
		return True
	elif pic == 'orphotdir/partialshade.jpg':
		return True
	elif pic == 'orphotdir/partialsun.jpg':
		return True
	elif pic == 'orphotdir/tempint.jpg':
		return True
	elif pic == 'orphotdir/temphot.jpg':
		return True
	elif pic == 'orphotdir/spring.jpg':
		return True
	elif pic == 'orphotdir/fall.jpg':
		return True
	elif pic == 'orphotdir/winter.jpg':
		return True
	elif pic == 'orphotdir/sun.jpg':
		return True
	elif pic == 'orphotdir/sun.jpg':
		return True
	else:
		return False

# returns a list of valid orchid pics. WORKS!
def getImgSources(link): 
	try:
		pageData = requests.get(link) 
		soup = bs(pageData.text, 'html.parser')
		images = soup.findAll('img')
		imgList = []

		for image in images:
			source = image['src']
			if isIcon(source) == False:
				imgList.append(image['src'])

		return imgList
	except:
		print("An error occurred in getImgSources.")

# take site's home URL as a string input, return list of index URLS as strings
def getIndexLinks(link):
	try:
		pageData = requests.get(link) 
		soup = bs(pageData.text, 'html.parser')
		linkList = soup.findAll('a')
		indexLinks = []

		for a in linkList:
			linkHref = str(a.get('href'))
			if ('http://www.orchidspecies.com/' + linkHref) in indexLinks:
				break
			elif (linkHref[:5] == 'index') and (linkHref != 'index.htm') and (linkHref[-1] == 'm'):
				indexLinks.append('http://www.orchidspecies.com/' + linkHref)
		return indexLinks
	except: 
		print("An error occurred in getIndexLinks.")

# take one of the index links as input, return a list of the species pages. WORKS!?
def getPageLinks(link):
	try:
		pageData = requests.get(link) 
		soup = bs(pageData.text, 'html.parser')
		speciesLinks = []

		for ol in soup.findAll('ol'):
			for li in ol.findAll('li'):
				for link in li.findAll('a'):
					if ('http://www.orchidspecies.com/' + str(link.get('href'))) in speciesLinks:
						break
					else:
						speciesLinks.append('http://www.orchidspecies.com/' + str(link.get('href')))

		return speciesLinks
	except:
		print("An error occurred in getPageLinks.")

#harvest links from the target webpage; optimized for 'http://www.orchidspecies.com/index.htm'
def harvestLinks(link):
	indexLinks = getIndexLinks(link)
	speciesLinks = []
	imagesList = []

	for i in indexLinks:
		speciesLinks = speciesLinks + getPageLinks(i)

	for b in speciesLinks:
		imagesList = imagesList + getImgSources(b)

	return imagesList

# it works! But it's slow. Maybe I can figure out a way to improve performance. If not, I can leave running for a few hours when I have the time.
