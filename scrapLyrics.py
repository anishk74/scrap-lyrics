from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
searchSong='https://www.google.com/search?q='
s=input('Enter the song to find its lyrics: ')
for i in s:
	if i==' ':
		searchSong+='+'	
	else:
		searchSong+=i
searchSong+='+lyrics'


options = webdriver.ChromeOptions();
options.add_argument('headless');
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",options=options)

driver.get(searchSong)

try:
	expand=driver.find_element_by_css_selector("div[aria-expanded='false']")
	driver.execute_script("document.querySelectorAll('div[aria-expanded=false]')[1].click()")
	driver.execute_script("arguments[0].setAttribute('area-expanded','true')", expand)

	e1=driver.find_element_by_class_name("bkWMgd")

	print(e1.text)
except:
	print('Couldn\'t find lyrics')

finally:
	driver.quit()
	



