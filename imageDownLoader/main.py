import random
import urllib.request

def image_downloader(url):
    name = random.randrange(1, 100)
    fileName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fileName)

image_downloader("http://cms.abo.fi/static/kuvat/logo-en.png")
