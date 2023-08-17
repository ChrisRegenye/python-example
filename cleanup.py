#!/usr/bin/env python
import sys
import json
diffs=open("./change.log")
d=json.load(sys.argv[1])
for difftype in d:
  changelog = []
  dt = difftype["DiffType"]
  print('----------------------------------')
  print("%s:\n----------------------------------" % dt.capitalize())
  if difftype["Diff"]["Packages2"]:
    print("New packages added:")
    for package in difftype["Diff"]["Packages2"]:
      print('| {:35}    {:15}'.format(package['Name'], package['Version']))
    print('\n')
  
  if difftype["Diff"]["Packages1"]:
    print("Old packages removed:")
    for package in difftype["Diff"]["Packages1"]:
      print('| {:35}    {:15}'.format(package['Name'], package['Version']))
    print('\n')
  
  if not difftype["Diff"]["InfoDiff"]:
    print("No version changes")
    print('\n')
    continue
  else:
    print('{:35}   {:15} -> {:10}'.format("The following versions have changed: ", "Old", "New"))
    for package in difftype["Diff"]["InfoDiff"]:
      if dt.capitalize() == "Pip": 
        changelog.append([package["Package"], package["Info1"][0]["Version"].split()[0], package["Info2"][0]["Version"].split()[0]])
      else:
        changelog.append([package["Package"], package["Info1"]["Version"].split()[0], package["Info2"]["Version"].split()[0]])
    for row in changelog:
      if row[0] == "nodejs":
        row[1] = row[1].split('-deb')[0] 
        row[2] = row[2].split('-deb')[0]
      if '~' in row[1] or '~' in row[2]:
        row[1] = row[1].split('~')[0] 
        row[2] = row[2].split('~')[0]
      if row[1] == row[2]:
        continue
      print('| {:35}   {:15} -> {:10}'.format(*row))
    print('\n')