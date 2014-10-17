import urllib2

cl_bike = ["http://minneapolis.craigslist.org/search/bia", "http://minneapolis.craigslist.org/search/bia?s=100&", "http://minneapolis.craigslist.org/search/bia?s=200&"]

page_source = ""

for x in cl_bike:
	response = urllib2.urlopen(x)
	page_source += response.read()
	
page_source = page_source.lower()

source_split = page_source.split()

road_count = 0
special_count = 0
giant_count = 0
felt_count = 0
cannon_count = 0
fuji_count = 0

road_split = []
road_string = ""
iter = 0
while iter != len(source_split):
	for x in range(iter, len(source_split)):
		road_string += source_split[x] + " "
		iter += 1
		if source_split[x] == "road":
			road_string += source_split[x] + " "
			for y in range(iter, len(source_split)):
				road_string += source_split[x] + " "
				if y == "<":
					road_split.append(road_string)
					break
				break
			break

for x in source_split:
	if x == "road":
		road_count += 1
	if x == "specialized":
		special_count += 1
	if x == "giant":
		giant_count += 1
	if x == "felt":
		felt_count += 1
	if x == "cannondale":
		cannon_count += 1
	if x == "fuji":
		fuji_count += 1

text_file = open("text_file.txt", "w")

output_string = ""

for x in source_split:
	output_string += x + " "

text_file.write(output_string)
text_file.close()

print "This is how many times 'road' shows up: ",
print road_count
print "This is how many times 'specialized' shows up: ",
print special_count
print "This is how many times 'giant' shows up: ",
print giant_count
print "This is how many times 'felt' shows up: ",
print felt_count
print "This is how many times 'cannondale' shows up: ",
print cannon_count
print "This is how many times 'fuji' shows up: ",
print fuji_count

for x in road_split:
	print x

"""print page_source"""