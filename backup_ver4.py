#!/usr/bin/env python3

import os
import time
import zipfile

# 1. The files and directories to be backed up are
# specified in a list.
source = ['/Users/cvine/projects']

# 2. The backup must be stored in a
# main backup directory
target_dir = '/Users/cvine/backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	print('Successfully created directory', target_dir)

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
today = target_dir + os.sep + time.strftime('%Y%m%d')

# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# initializing empty file paths list
file_paths = []
# crawling through directory and subdirectories
for directory in source:
	for root, subdirectories, files in os.walk(directory):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')

# Check if a comment was entered
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(" ", "_") + '.zip'

# Create target directory if it is not present
if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)

# 5. Writing files to a zipfile
print('Running:')
with zipfile.ZipFile(target, 'w') as zipArchive:
	for file in file_paths:
		print('  adding:', file)
		zipArchive.write(file)

print('Successful backup to', target)
