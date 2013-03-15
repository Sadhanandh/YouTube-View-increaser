#! /usr/bin/env python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random
import os

word_n = "hello + Martin Solveig "
search_link_w = "watch?v=pvdrQpbkKWY"
max_n = 6
iter_n = 1
min_t =2
max_t = 3

def cheatyoutubeff(word_n,search_link_w,max_n,iter_n,min_t,max_t):

	fp = webdriver.FirefoxProfile(os.path.join(os.path.abspath("."),'support/User-Agents/UA'+str(iter_n)))
	browser = webdriver.Firefox(fp) # Get local session of firefox
	#browser.get("http://ifconfig.me") # Load page
	#time.sleep(3)

	browser.get("http://www.youtube.com") # Load page
	elem = browser.find_element_by_name("search_query")
	elem.send_keys(word_n + Keys.RETURN)

	rand_link =True
	rand_x= random.randrange(0,3)

	for x in range(max_n):
		time.sleep(random.randrange(min_t,max_t))
		try :
			if rand_link and x==rand_x:
				r_li_num = random.randrange(1,6)
				elem = browser.find_element_by_xpath("id('search-results')/li["+str(r_li_num)+"]/div[2]/*/a")
				elem.click()
				time.sleep(8)
				browser.back()

			e = browser.find_element_by_xpath("//a[contains(@href,'"+search_link_w+"')]")
			e.click()
			print "Found the link @ "+str(x+1)+" Page"
			break
		except NoSuchElementException as e:

			elem = browser.find_element_by_xpath("//a[contains(@href,'&page="+str(x+2)+"')]")
			elem.click()

	else:
		print "Didnt find the Url in any of the "+str(max_n)+" Pages."
	#browser.close()	
	
if __name__ == '__main__':

	cheatyoutubeff(word_n,search_link_w,max_n,iter_n,min_t,max_t)
