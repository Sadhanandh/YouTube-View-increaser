#!/usr/bin/env python
import re
import os
from support import ffyoumod as browsermod

settingsfile = "youtubeconfig.ini"
query_word = "hello"
s_url = "http://en.wikipedia.org/wiki/HelloWorld"
max_n =10
min_rand = 2
max_rand = 10
no_time = 2

if os.path.exists(settingsfile):
	fr = open(settingsfile)
	data = fr.read()
	ma = re.findall("Url\s*:\s*(\S+)",data,re.IGNORECASE)
	if ma != []:
		s_url = ma[0]
	ma = re.findall("Word\s*:\s*(\S+.*)",data,re.IGNORECASE)
	if ma != []:
		query_word = ma[0]
	ma = re.findall("Max\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		max_n = int(ma[0])
	ma = re.findall("Min\s*Time\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		min_rand = int(ma[0])
	ma = re.findall("Max\s*Time\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		max_rand = int(ma[0])
	ma = re.findall("No\s*of\s*Times\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		no_time = int(ma[0])
	fr.close()



print s_url,query_word,max_n,min_rand,max_rand

for x in range(no_time):
	browsermod.cheatyoutubeff(query_word,s_url,max_n,x+1,min_rand,max_rand)
	#if using_tor:
	#	browsermod.changeip(tor_host,tor_port,tor_pass)
