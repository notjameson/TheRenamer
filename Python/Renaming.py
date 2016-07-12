#!/usr/bin/env python

# -- JPG RENAMING SCRIPT --
# This little program batch renames all of Cole Haan, LLC's photos
# When they receive them from the photography studio, the naming convention is different
# from what they use on the website. This renames them all instead of the user having to do it one-by-one.
# 

# get dat OS
import os

# Searches through computer's file system to find directory with name matching the arg passed through
def find(fileName):
	for root, dirs, files in os.walk("./"):
		# If we find the file do this, else, let us know it wasn't found
		if fileName in root:
			nameChange(fileName)
			print "Have a nice day :)"
			print ""
		else:
			print "Folder not found"
			# folderName = input('Enter the folder name manually here: ')
			# nameChange(folderName)

def nameChange(name):
	lst = os.listdir(name)
	print ""
	for image in lst:
		# Will implement separate case for jpeg (or probably change the code here to start from
		# before the period)
		if image[len(image) - 4:] == (".jpg" or ".Jpg" or ".JPG"):
			# Grab the character
			character = image[len(image) - 12:len(image) - 11]

			# and the SKU
			sku = image[len(image) - 10:len(image) - 4]

			# This is where we make the new file name (in format SKU_CHARACTER)
			# Immediately below is if the PHOTO STUDIO DOESNT NAME OUTERWEAR CORRECTLY
			if character == "M":
				character = "A"
			elif character == "N":
				character = "B"
			elif character == "O":
				character = "C"
			elif character == "P":
				character = "D"
			newName = sku + "_" + character + ".jpg"

			# Print for reassurance
			print image + " is now renamed to " + newName
			print ""

			# This is the key line, locates the file and renames it (without affecting the file itself)
			os.rename(name + "/" +image, name + "/" +newName)

# THIS WILL CHANGE DEPENDING ON YOUR PERSONAL FILE SYSTEM NAME
# IT IS NECESSARY TO CHANGE THE PARTS IN QUOTES AND THEN UNCOMMENT
find("./Images")
# Kinda cool how the main "method" is only one line of code