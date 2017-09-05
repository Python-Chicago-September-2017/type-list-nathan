testList = ["magical unicorns",19,"hello",98.98,"world"]

newString = "String:"
numSum = 0
for i in range(0, len(testList)):
    typeOfData = type(testList[i])
    if (typeOfData == int or typeOfData == float):
        numSum += testList[i]
    else:
        newString += " " + testList[i]

if (numSum > 0 and newString != "String:"):
    print "The list you entered is of mixed type"
    print newString
    print "Sum: " + str(numSum)
elif (sum > 0 and newString == "String:"):
    print "The list you entered is of interger type"
    print "Sum: " + str(numSum)
elif (sum == 0 and newString != "String:"):
    print "The list you entered is of string type"
    print newString
