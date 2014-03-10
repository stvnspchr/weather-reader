import csv
import urllib2
import StringIO
import os

# Set date range for weather data pull
begin_month = 1
end_month = 3
begin_day = 1
end_day = 10

for m in range(begin_month,end_month):				# Months
	for d in range(begin_day,end_day):				# Days
		# Open webpage and read data
		url = 'http://www.wunderground.com/history/airport/KMLE/2014/' + str(m) + '/' + str(d) + '/DailyHistory.html?req_city=Ashland&req_state=NE&req_statename=Nebraska&format=1'
		print "reading webpage on " + str(m) + '/' + str(d)
		page = urllib2.urlopen(url)
		cr = csv.reader(page)
		
		# Check for subdirectory and/or make subdirectory
 		path = "data"
 		if not os.path.exists(path):
 			os.makedirs(path)
			
		# Create file and write data
		filename = "weather-data-" + str(m) + '-' + str(d) + ".tsv"
		file = open(os.path.join(path, filename), "wb")
		cw = csv.writer(file, delimiter='\t')
		print "writing file of " + str(m) + '/' + str(d)
		for row in cr:
			cw.writerow(row)
			
		# Close file
		print str(m) + '/' + str(d) + " file closed"
		file.close()
			
print ".... done!"
