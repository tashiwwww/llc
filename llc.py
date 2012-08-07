tablefile = open("in/table.tbl")
table = {}
for line in tablefile:
	line = line.rstrip('\n')
	splits = line.split("=")	
	table[splits[0]] = splits[1]
#print(table)
tablefile.close()

script = open("in/script.txt")
linecount = 0
allvwf = list()
allfwf = list()
vwfstr = list()
fwfstr	 = list()

for line in script:
	linecount += 1
	realline = line[1:-1]
	linelength = len(realline)
	fwfpx = linelength*16
	vwfpx = 0
	#print(line)
	for letter in realline:
		try:
			vwfpx += int(table[letter])
		except KeyError:
			vwfpx += 16 
	allvwf.append(vwfpx)
	allfwf.append(fwfpx)

fwflines = sum(allfwf)//linecount
vwflines = sum(allvwf)//linecount

print(linecount,"total lines.")
print("Average line length with fixed-width:",fwflines)
print("Average line length with variable-width:",vwflines)
print("Diff per string:",fwflines-vwflines, "px, or approximately",(fwflines-vwflines)//12, "extra letters")

