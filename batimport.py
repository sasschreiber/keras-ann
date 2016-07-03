import csv

###
# Format of input file lines: NAME 22 34 54 .....\n\n
###

fileName = "minitrain"

txt_file = fileName + ".dat"
csv_file = fileName + ".csv"

totaloutputs = 39
uniquenamecounter = 0
lastname = ""

def getBinaryOutput(length, positionOfOne):
	outputlist = ['0']*length
	outputlist[positionOfOne] = '1'
	return outputlist

with open(txt_file, "rt", encoding="utf-8") as tf, open(csv_file, "wt", encoding="utf-8", newline='') as cf:
    reader = csv.reader(tf, delimiter=' ')
    writer = csv.writer(cf)
    for row in reader:
    	#remove empty parameter at the end
    	if (row[-1] == ""):
    		row.pop()
    	
    	if ((row[0] != lastname) and (lastname != "")):
    		uniquenamecounter += 1

    	lastname = row[0]
    	del row[0]
    	row = row + getBinaryOutput(totaloutputs, uniquenamecounter)
    	# print(row)
    	# print()
    	# print()
    	print(len(row))
    	writer.writerow(row)