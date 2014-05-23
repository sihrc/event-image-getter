import urllib2, urllib, simplejson
from test_events import test_events
import os

def getImages(event):
	page = 0
	query = "v=1.0&q=%s&rsz=8&start=%d" % (event, page * 8)
	results = simplejson.load(urllib2.urlopen(url + query))

	filepath = os.path.join("images", (event.name.replace(" ","_").replace("/","-")))
	for i, image in enumerate([result['unescapedUrl'] for result in results['responseData']['results']]):
		urllib.urlretrieve(image, filepath + ".%d.jpg" % i)
	

if __name__ == "__main__":
	url = 'https://ajax.googleapis.com/ajax/services/search/images?'
	for event in test_events:
		getImages(event)
	
