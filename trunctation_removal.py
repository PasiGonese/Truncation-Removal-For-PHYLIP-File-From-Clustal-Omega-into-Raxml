#!/usr/bin/env python3

# import argparse library
import argparse
import re
import random

# create parser object
parser = argparse.ArgumentParser()

# create argument group
required = parser.add_argument_group('Required arguments')

# add argument to group
required.add_argument('-i', '--input', type=str, help='Path to input file', required=True)

# parse the arguments into variables
args = parser.parse_args()

# open file
file_in = open(args.input)

# read file contents
lines = file_in.readlines()

head = []
seq = []

for line in lines:
    line.strip()
    if line[0] == ">":
        head.append(line)
    if line[0] != ">":
        seq.append(line.rstrip("\n"))


print(len(head))

file_in.close()

main_file_in = open(args.input)

lines2 = main_file_in.readlines()

header2 = []
sequence2 = []
i = 0

header2.append(lines2[0].rstrip("\n"))

for line in lines2:
    line.strip()
    sequence2.append(line.rstrip("\n"))
    

print(lines2[3])
      
print(len(lines2[9]))

print(lines2[9])

special_collection = []
for i in lines2:
        if i[0].islower():
            special_collection.append(i.rstrip("\n"))


res = []
for i in special_collection:
    for j in i:
        if(j.isupper()):
            i = i.replace(j, " "+j, 1)
            break
        elif(j == "-"):
            i = i.replace(j, " "+j, 1)
            break            
    res.append(i)
 
# printing result
print("The space added list of strings : " + str(res))

print(header2)
# print(sequence2)

# print(lines2[7])
unwanted = [0,1,2,3,4,5,6,7]


for ele in sorted(unwanted, reverse = True):
    del sequence2[ele]




connector = "\n"


str_header2 = ""
str_header2 = connector.join(map(str,header2))

str_res = ""
str_res = connector.join(map(str,res))

str_sequence = ""
str_sequence = connector.join(map(str,sequence2))



outputfile = open('untruncated.phylip', 'w')
outputfile.write(str(str_header2) + "\n")
outputfile.write(str(str_res) + "\n")
outputfile.write(str(str_sequence) + "\n")
outputfile.close()