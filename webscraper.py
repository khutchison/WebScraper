import requests 
from bs4 import BeautifulSoup as bs

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

# returns a list of valid orchid pics 
def getURLS(link):

	pageData = requests.get(link) 
	soup = bs(pageData.text, 'html.parser')
	images = soup.findAll('img')
	imgList = []

	for image in images:
		source = image['src']
		if isIcon(source) == False:
			imgList.append(image['src'])

	return imgList

