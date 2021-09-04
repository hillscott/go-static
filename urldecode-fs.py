#!/usr/bin/python3
# Author Ian Reynolds
# Set the below variable to where you want the script to walk through your file-system
# It will find any folders that have % characters in them, which is a common outcome
# when using Simply Static on non-ASCII character URLs within Wordpress
# Once located, the script will use urllib to translate the %-encoded name to UTF characters.
# Ensure your file-system supports non-ASCII file-names!
# NOTE: If your site also has non-ASCII file-names, this script will need edits to function.
# GPLv2 Licensing
from urllib.parse import unquote
import os
import shutil
osdirLoc = "/INSERT-FS-PATH-HERE/"

if ("/INSERT-FS-PATH-HERE/" in osdirLoc):
  print("Please set the ospath variable to continue...")
  print("USE CAUTION: DATA WILL BE DESTROYED!")
  print("DO NOT USE unless you understand this script")
  quit()
for root, dirs, files in os.walk(osdirLoc, topdown=False):
   for name in files:
       if ('%' in name):
           print("FILE Encoding issue found! Doing nothing!")
           print(os.path.join(root, name))
   for name in dirs:
       if ('%' in name):
           print("DIR Encoding issue found!")
           path = os.path.join(root, name)
           print(path)
           value = unquote(path)
           print(value)
           if (os.path.isdir(value)):
               print("Translated dir already exists...")
               print("Will copy " + path + " To: " + value)
               shutil.rmtree(value)
               shutil.copytree(path, value)
           else:
               print("Will copy " + path + " To: " + value)
               shutil.copytree(path, value)
