#!/usr/bin/env python
from zipfile import ZipFile
import sys
import argparse

desc = "Brute force Zip files using a dictionary attack"
options = argparse.ArgumentParser(description=desc)
options.add_argument("-z", "--zip", dest="zip")
options.add_argument("-d", "--dictionary", dest="dict")

args = options.parse_args()

if(args.zip == None):
    print "Error, please specify a zip file to crack"
    exit(1)
    
zipFileName = args.zip
#default unless a dictionary is specified...
dictionary = "dictionary.txt"
if(args.dict):
    dictionary = args.dict

status = 'Password not found...\n'

zf = ZipFile(zipFileName)

print("Checking...\n")

with open(dictionary, 'r') as dict:
    for potentialPWDs in dict.readlines():
        potentialPWD = potentialPWDs.strip('\n')
        try:
            print("Trying... %s") % potentialPWD
            zf.extractall(pwd=potentialPWD)
            status = 'Found! Password: %s' % potentialPWD
            break
        except:
            pass
print(str(status))
    
        
