#!/usr/bin/env python
import sys
import os
import re

def low(z):
    return z.lower()


dict2={}
the_dict={}
i=0
d={}

#Convert dictionary from file to actual dictionary
for line in sys.stdin:
	x =line.split(":")
        a=x[0]
        a=re.sub(r'[^\w\s]','',a)
        b=x[1]
        b=re.sub(r'[^\w\s]','',b)
        b=re.sub(r'\b\w{1,3}\b', '',b) #Filter : remove words with up to 3 characters
	b=b.strip('\n')
	b=b.strip('\t')
	b=b.strip(' ')
        d[a]=b

dict2.update(d)

###Inverted Index

for key in dict2:
	values=dict2.get(key)
	values=values.split(' ')
	for value in values:
		if value not in the_dict : # Create empty dictionary is value not included
			the_dict[value]=[]
 			the_dict[value].append(1)
			the_dict[value].append([key])

##Or update
		else:
			the_dict[value][0]+=1 #How many times the value appeared
			the_dict[value][1].append(key)


#######Print results
ld = list(the_dict)
ld.sort(key=low)
for k in ld :
	print(k,the_dict[k][1])
