from urllib import urlopen
import urllib
import nltk
import re

# page = urlopen("http://www.a1consolidated.com.au/").read()
# page = urlopen("http://www.abmresources.com.au/").read()
# url = "http://www.adelaideresources.com.au/"
# url = "http://www.gascoyneresources.com.au/"

# page = urlopen("http://www.a1consolidated.com.au/investor-centre/asx-announcements/").read()
# # print page[:60]


# # cPage = nltk.clean_html(page)
# # print cPage[:100]

# lPdf = re.findall('<a href="([^"]+\.pdf)"', page)
# # print len(lPdf)
# print lPdf[:5]

##### read online pdf incorrectly but may be useful
# pdf = urlopen("http://www.a1consolidated.com.au/images/uploads/Resignation_of_Director_and_Final_Directors_Interest_Notice.pdf").read()
# print pdf[:500]
# print len(pdf)


##### first trial download a pdf from website
# url = "http://www.a1consolidated.com.au/images/uploads/Resignation_of_Director_and_Final_Directors_Interest_Notice.pdf"
# print "downloading with urllib"
# urllib.urlretrieve(url, "goldnerds1.pdf")

linksPage = urlopen("http://goldnerds.com.au/").read()
urls = re.findall('<a href="(http://[^"]+)"', linksPage)
countErrorSites = {"failUrl":[], "noneAnnoucement":[], "failAnnoucements":[]}

##### loop all the http:// links within linksPage
for i in range(len(urls)-235):
	print "\n##### %d site #####" % i

	url = urls[i]
	
	while url[-1] == '/':
		url = url[:-1] ##### get rid of the '/' at the end of url
	
	print "url is \""+url+"\""

	try:
		urlopen(url).read()
	except IOError:
		print "----- cannot read url -----"
		countErrorSites['failUrl'].append(url) ##### record inaccessible urls
		continue
	else:
		sourceHome = urlopen(url).read()

	hrefsHome = re.findall('<a href="([^"]+)"', sourceHome)
	for hrefA in hrefsHome:                                                                                     
		if re.findall('(?i)announcement', hrefA):
			urlAnnounce = hrefA

	try:
		urlAnnounce
	except NameError:
		print "----- no annoucement page -----"
		countErrorSites['noneAnnoucement'].append(url)
		continue
	else:
		if not re.findall('http://', urlAnnounce):
		        while(urlAnnounce[0] == '/'):
		                urlAnnounce = urlAnnounce[1:] ##### get rid of all '/'s at the end of announcement url 
		        urlAnnounce = url+'/'+urlAnnounce
		print urlAnnounce
                        

	try:
		urlopen(urlAnnounce).read()
	except IOError:
		print "----- cannot read annoucement page -----"
		countErrorSites['failAnnoucements'].append(url)
		continue
	else:
		sourceAnnounce = urlopen(urlAnnounce).read()

	hrefsPdf = re.findall('<a href="([^"]+.pdf)"', sourceAnnounce)
	print "pdfs on announcement page:"
	print hrefsPdf
	##### keep record of links of pdfs in urls
	if len(hrefsPdf) > 0:
		f = open('files/linksOfPdfsInURLs.txt', 'a+')
		f.write(url+":\n")
		for hrefPdf in hrefsPdf:
			f.write(hrefPdf+"\n")
		f.write("\n\n")
		f.close()

	reports = []
	for hrefP in hrefsPdf:
		# if re.findall('(?:A|a)nnual', hrefP):
		if re.findall('(?i)preliminary[\w\W]?economic[\w\W]?assessment|(?i)scope|(?i)technical|annual', hrefP):
			if not re.findall('http://', hrefP):
				while(hrefP[0] == '/'):
					hrefP = hrefP[1:]
				hrefP = url+'/'+hrefP
			if hrefP not in reports:
				reports.append(hrefP)
	print "!!!!!List of useful reports:"
	print reports

	if len(reports) > 0:

		def callbackfunc(blocknum, blocksize, totalsize):
		    percent = 100.0 * blocknum * blocksize / totalsize
		    if percent > 100:
		    	percent = 100
		    print "%.2f%%"% percent

		print "downloading reports....."
		j = 0
		for report in reports:
			nameReport = "files/"+report.split('/')[-1]
			urllib.urlretrieve(report, nameReport, callbackfunc)
			j += 1
			print "%d pdf downloaded" % j
