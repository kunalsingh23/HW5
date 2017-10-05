import re

hand = open('sumfile.txt')

listofnums = []

for line in hand:
	line = line.rstrip()
	group = re.findall('[0-9]+', line)
	if len(group) >= 1:
		listofnums.append(group)
	else:
		pass

finallist = []

for group in listofnums:
	for x in group:
		finallist.append(int(x))


count = 0

for x in finallist:
	count += x


print (count)



