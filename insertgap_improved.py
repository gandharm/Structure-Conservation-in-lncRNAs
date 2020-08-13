#!/usr/bin/python

#Updated, modified, and scaled insertgap.py script
#by Gandhar Mahadeshwar
#Pyle Lab - Yale University

import sys

with open(sys.argv[1],'r') as sequenceFile:
	seq = sequenceFile.readlines()

with open(sys.argv[2],'r') as structureFile:
	struc = structureFile.readlines()

seqlist = []
struclist = []

for x in seq:
	x = x.replace('\n', '')
	seqlist.append(x)
for y in struc:
	y = y.replace('\n', '')
	struclist.append(y)

if len(seqlist) != len(struclist):
	print ("STOP. Sequence LIST is not the same size as structure LIST.")
	sys.exit()

#with open(sys.argv[1],'r') as sequenceFile:
#	seq = sequenceFile.read().replace('\n', '')

#with open(sys.argv[2],'r') as structureFile:
#	struc = structureFile.read().replace('\n', '')

output = open("out.txt",'w')

#print (seq)
#print (len(seq))
#print (struc)
#print (len(struc))
#print(seqlist)

l = 0
while l < len(seqlist):
	indivseq = seqlist[l]
	indivstruc = struclist[l]
	i = 0
	while i < len(indivseq):
		if indivseq[i] == '-':
			indivstruc = indivstruc[:i]+'-'+indivstruc[i:]
		i +=1
	print (indivstruc)
	print(len(indivseq))
	print(len(indivstruc))
	output.write(indivstruc)
	output.write('\n')
	if len(indivstruc) != len(indivseq):
		print ("STOP. Sequences are not the same length. Something is wrong. No output file has been created.")
		print ("Error occurred at seq (printed above) number: ", l+1)
		sys.exit()
	l +=1

#print (len(struc))

output.close


#file1 = open(sys.argv[1],'r')
#file2 = open(sys.argv[2],'r')
#file3 = open("out.txt",'w')

#Seq = file1.read();
#Ss = file2.read();

#l = len(Seq);

#for i in enumerate(Seq):
#	if Seq[i] == '-':
#		Ss = Ss[:i]+'-'+Ss[i:]

#print (Seq)
#print (Ss)

#file3.write(Ss);
#file3.close();
