#!/usr/bin/python
import sys
import re

name = []
phyl = []
info = []
lst = []

a = ['genera', 'species', 'famil', 'order', 'genus', 'class']
pat = r'(?<=\().+?(?=\))'
filename = sys.argv[1]
o_string = open(filename, "r")

for line in o_string:
	temp = line.split()
	phyl.append(temp[0])
	name.append(temp[1])
	lst = re.findall(pat, line)
	if lst:
		if any (x in lst[0] for x in a):
			try:
				info.append(lst[0])
			except IndexError:
				info.append("")
		else:
			try:
				info.append(lst[1])
			except IndexError:
				info.append("")
	else:
		info.append("")

zip(phyl, name, info)

textfile = open("parsed.txt", "w")

for i,j,k in zip(phyl, name, info):
	textfile.write("%s %s %s\n" % (i,j,k))
