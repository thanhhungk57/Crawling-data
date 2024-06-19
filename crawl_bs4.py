from bs4 import BeautifulSoup
import urllib.request

url =  'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feed = soup.find('section', class_='featured container clearfix').find('a')
title = new_feed.get('title')
link = new_feed.get('href')
print('Title: {} - Link: {}'.format(title, link))
