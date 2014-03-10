import csv
import urllib2
import StringIO

for m in range(1,4):
	for d in range(1,3):
		url = 'http://www.wunderground.com/history/airport/KMLE/2014/' + str(m) + '/' + str(d) + '/DailyHistory.html?req_city=Austin&req_state=TX&req_statename=Texas&format=1'
		print url
		page = urllib2.urlopen(url)
		cr = csv.reader(page)
	
		file = open("weather-data-" + str(m) + '-' + str(d) + ".tsv", "wb")
		cw = csv.writer(file, delimiter='\t')
		for row in cr:
			cw.writerow(row)