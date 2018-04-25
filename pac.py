#!/usr/bin/python

import urllib.request
import re


url="http://news.cnfol.com/it/20180331/26226895.shtml"


pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")

#pat='<img src="(.*?)" width="'
pat="<center><a href='(.*?)' target='_blank'>"
datalist=re.compile(pat,re.S).findall(pagedata)
for i in range(0,len(datalist)):
	print(datalist[i])
	
