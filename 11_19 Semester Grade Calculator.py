#!/usr/bin/env python

currect = float(raw_input("What is your current grade percentage? "))
weight = float(raw_input("What percentage of your semester grade is the Final? "))


if currect >= 90:
    grade = "A"
elif currect >= 80:
    grade = "B"
elif currect >= 70:
    grade = "C"
elif currect >= 60:
    grade = "D"
else:
    grade = "F"

if grade == "A":
    print "To keep your A, you must score a " + str((90 - (currect*(1-weight/100)))/(weight/100)) + "% on the final."
if grade =="B":
    print "To keep your B, you must score a " + str((80 - (currect*(1-weight/100)))/(weight/100)) + "% on the final."
    if (90 - (currect*(1-weight/100)))/(weight/100) <= 100:
        print "You must score a " + str((90 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to an A."
    else:
        print "It is not possible to raise your grade to an A."
if grade == "C":
    print "To keep your C, you must score a " + str((70 - (currect*(1-weight/100)))/(weight/100)) + "% on the final."
    if (80 - (currect*(1-weight/100)))/(weight/100) <= 100:
        print "You must score a " + str((80 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to a B."
    else:
        print "It is not possible to raise your grade to an B."
if grade == "D":
    print "To keep your D, you must score a " + str((60 - (currect*(1-weight/100)))/(weight/100)) + "% on the final."
    if (70 - (currect*(1-weight/100)))/(weight/100) <= 100:
        print "You must score a " + str((70 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to a C."
    else:
        print "It is not possible to raise your grade to an C."
if grade == "F":
    if (60 - (currect*(1-weight/100)))/(weight/100) <= 100:
        print "You must get a " + str((60 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to get a D."
    else:
        print "It isn't possible for you to pass this class."