# -*- coding: utf-8 -*-
import os
import nltk
import re
##from collections import OrderedDict
from operator import itemgetter
 
path = 'files/'
listing = os.listdir(path)
##for infile in listing:
##    print "current file is: " + infile

##for aFile in listing:
##	filePath = 'files/' + aFile
##	f = open(filePath, 'r').read()
##	##f.read()
##	##for line in f:
##	##    print line[:-1]
##
##	##f1 = re.findall('Table \d+\.\d+[\w\W]*?\.{2,}', f)
##	##f1 = re.findall('Table \d+\.\d+', f)
##
##	##for table in f1:
##	##    print table + "\n"
##
##	projectCandidates = re.findall('((?:[A-Z]\w*\s)+Project)', f)
##
##	projectDict = nltk.defaultdict(int)
##	for project in projectCandidates:
##	    projectDict[project] += 1
##
##	##sorted(projectDict.items(), key = itemgetter(1))
##	##sorted(projectDict.items(), key = lambda x: x[1])[-1]
##	##sorted(projectDict.items(), key = lambda x: x[1], reverse=True)[0]
##	pD = dict(zip(projectDict.values(), projectDict.keys()))
##	if not pD:
##		continue
##	print str(max(pD))+' of '+pD[max(pD)]+"\nis the project name of report <-- "+aFile+" -->\n"

filePath = 'files/0lex_current.txt'
f = open(filePath, 'r').read()
tableInfo = re.findall('Mineral Resource Statement of the Joyce Lake DSO Iron Deposit[\w\W]*?numbers', f)
##((?:Table 1.1 ﾨC Mineral Resource Statement of the Joyce Lake DSO Iron Deposit)[\w\W]*?(?:\s*?\r?\n\s*?){3})

f2 = open('tableInfo.txt', 'w+')
f2.write(tableInfo[2])
f2.close()
