import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


term=0.1
current_dir=os.getcwd()
driver_dir=current_dir+'\\chromedriver.exe'
print(driver_dir)

url="https://gallog.dcinside.com/"

print('ID : ',end='')
user_id=input()

print('PW : ',end='')
pw=input()

gallog_url=url+user_id+"/posting"
print(gallog_url)
driver = webdriver.Chrome(driver_dir)   # chromedriver   link: https://chromedriver.storage.googleapis.com/index.html?path=2.35/
driver.get(gallog_url)

driver.find_element_by_xpath('//*[@id="top"]/div[1]/div/div/ul/li[6]/a').click()
driver.find_element_by_name('user_id').send_keys(user_id)
driver.find_element_by_name('pw').send_keys(pw)
driver.find_element_by_xpath('//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()


#move article list 
driver.find_element_by_xpath('//*[@id="container"]/article/div/ul/li[2]/a').click()
#if article list not empty then delete all post list
while True :
	driver.refresh()
	time.sleep(term)
	html=driver.page_source
	soup=BeautifulSoup(html,'html.parser')
	state=soup.select('#container > article > div > section > div.gallog_cont > div.cont_box > div.gallog_empty')
	#if article list empty exit loop state
	if(len(state)==0) :
		check=driver.find_element_by_xpath('//*[@id="container"]/article/div/section/div[1]/div/ul/li[1]/div[2]/div/button')
		check.click()
		alert=driver.switch_to_alert()
		alert.accept()
		time.sleep(term)
		driver.refresh()
		time.sleep(term)
	elif(len(state)==1):
		print('Delete All Article')
		break

		
		
#move comment list
driver.find_element_by_xpath('//*[@id="container"]/article/div/ul/li[3]/a').click()
#if comment list not empty then delete all comment list
while True:
	###container > article > div > section > div.gallog_cont > div > div
	driver.refresh()
	time.sleep(term)
	html=driver.page_source
	soup=BeautifulSoup(html,'html.parser')
	state=soup.select('#container > article > div > section > div.gallog_cont > div.cont_box > div.gallog_empty')
	#if comment list empty exit loop state
	if(len(state)==0) :
		check=driver.find_element_by_xpath('//*[@id="container"]/article/div/section/div[1]/div/ul/li[1]/div[2]/div/button')
		check.click()
		alert=driver.switch_to_alert()
		alert.accept()
		time.sleep(term)
		driver.refresh()
		time.sleep(term)
	elif(len(state)==1):
		print('Delete All Comment')
		break
#exit cleaner
time.sleep(1)
driver.quit()
