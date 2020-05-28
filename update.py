#!/bin/env python2
#code owner = "Pakde"
#
import urllib2
import os

ver = open("version.txt", "r")
version = ver.read()
ver.close()

up = urllib2.urlopen("https://raw.githubusercontent.com/Aka-pakde/hacked/master/version.txt").read()
if version != up:
	print ""
	print "[+] Update available"
	print ""
	x = raw_input("Want to update y/n: ")
	if x == "y":
		os.remove("hacked.py")
		Aka-pakde = "https://raw.githubusercontent.com/Aka-pakde/hacked/master/hacked.py"
		update = urllib2.urlopen(Aka-pakde).read()
		
		hacked = open("hacked.py", "w")
		hacked.write(update)
		hacked.close()

		os.remove("version.txt")
		ver = open("version.txt", "w")
		ver.write(up)
else:
	print ""
	print "[-] No update available right now"
	print ""
