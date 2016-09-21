#Instructions
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailaddress = dict() #creating dictionary

for line in handle:
    word = line.split()
    if line.startswith('From '):
        mailaddress[word[1]] = mailaddress.get(word[1], 0) + 1      	

maxval = None
maxkee = None
for kee, val in mailaddress.items() :
	if maxval == None or maxval < val : 
		maxval = val
		maxkee = kee
	# print kee, val, maxkee, maxval
print maxkee, maxval
