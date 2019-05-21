import requests
import urllib.request
import os
from bs4 import BeautifulSoup
from google_images_download import google_images_download

def spider(txtpath):
   productlist = [] 
   file = open(txtpath, 'r')
   exitList = file.readlines()
   file.close()
   
   productlist.extend(exitList)
   page = 0
   max_pages = len(productlist)
   response = google_images_download.googleimagesdownload()
   while page < max_pages:
       aux = productlist[page].rstrip()
       #define search params:
       search_params = {
       "keywords": aux,
           "limit": 15,
           "size": "large",
           "print_urls": True,
           "output_directory": r"C:\Users\Agustin\Desktop\Crawler"
       }
       absolute_image_paths = response.download(search_params)
       print(absolute_image_paths)
       page += 1 

 
txtpath = r'C:\Users\Agustin\Desktop\Crawler\Input.txt'
spider(txtpath)