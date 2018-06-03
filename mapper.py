#!/usr/bin/env python
"""mapper.py"""



import os
import re
import string
import sys
from string import punctuation

#Iniitilization
dict2={}
dict={}
list=[]

#Remove whitespace and space
def strip_list_noempty(mylist):
    newlist = (item.strip() if hasattr(item, 'strip') else item for item in mylist)
    return [item for item in newlist if item != '']


###Remove xml tags
def strip_list_xml_tags(mylist):
    return re.sub('<[^<]+>', "",mylist)


#Input comes from STDIN (standard input)
for line in sys.stdin:
	word= strip_list_xml_tags(line)
	words=str(word).split()
	tokenized_sent = [w for w in words]
	tokenized_pun=[re.sub(r'[^\w\s]','',l) for l in words] #Remove punctuation
	tokenized_space=strip_list_noempty(tokenized_pun)

	list=[token for token in tokenized_space]
	key=os.readlink('/proc/self/fd/0').split(":")
	key=key[1]
	dict[key]= list
print(dict)
