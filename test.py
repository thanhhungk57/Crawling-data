# from bs4 import BeautifulSoup
# import urllib.request

# url = 'https://vnexpress.net'
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')

# # Tìm tất cả các thẻ 'a' có thuộc tính 'title'
# new_feed = soup.find('a', title=True)
# if new_feed:
#     title = new_feed.get('title')
#     link = new_feed.get('href')
#     print('Title: {} - Link: {}'.format(title, link))
# else:
#     print("Không tìm thấy thẻ 'a' nào có thuộc tính 'title'.")


from bs4 import BeautifulSoup
import urllib.request

url =  'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find('section', class_='section section_topstory').find_all('a')
for feed in new_feeds:
	title = feed.get('title')
	link = feed.get('href')
	print('Title: {} - Link: {}'.format(title, link))