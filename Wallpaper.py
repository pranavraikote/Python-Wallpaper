#Wallpaper of the day

#Import the modules 
import ctypes
from bs4 import BeautifulSoup
import requests
import urllib.request

#Open the website
res=requests.get('https://bingwallpaper.com/')
print('Getting the image')

#Assign a soup object for parsing
soup=BeautifulSoup(res.text,'lxml')

#Find the tag in which image is located
image_box=soup.find('a',{'class':'cursor_zoom'})

#Get the image
image=image_box.find('img')

#Get the url to download the image
link=image['src']

#Get the image file and save it in the present-working-directory
urllib.request.urlretrieve(link,'new.jpg')
print('Image downloaded')

#Image path
#Please set this path as the current working directory or in the directory where this script is placed and executed
path='E:\\Projects\\Wallpaper\\new.jpg'

#Set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
print('Wallpaper set succesfully')
