import random

#Create a sample list with 100 randomized numbers
samplelist = random.sample(xrange(0,10001),100)

# print samplelist

# for num in range(len(aList)):
# 	least = num 
# 	for num1 in range(num+1,len(aList)):
# 		if aList[num1] < aList[least]:
# 			least = num1		
# print aList

# def swap (aList, x, y):
# 	temp = aList[x]
# 	aList[x] = aList[y]
# 	aList[y] = temp
# 	print aList


#Implement a selection sort algorithm that returns a new list without creating another list

def selectionsort(aList):
	for x in range(len(aList)):
		for y in range(x+1,len(aList)):
			if aList[x] > aList[y]:
				aList[x],aList[y] = aList[y], aList[x]
	print aList

selectionsort(samplelist)


