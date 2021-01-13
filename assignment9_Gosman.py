#########################################################
#                                                       #
#   Seamus Gosman                                       #
#   CIS 211                                             #
#   Spring 2020                                         #
#   Assignment 9                                        #
#                                                       #
#########################################################
import sys
######################## Node Class ####################################################################################

class Team:                                                                 # team class
    def __init__(self, team, year):                                         # initializer
        self.year = year                                                    # set year
        self.team = team                                                    # set team

    def getName(self):                                                      # get name
        return self.team                                                    # return team name

    def getYear(self):                                                      # get year
        return self.year                                                    # return team year

    def printTeam(self):                                                    # print team
        print(self.team)                                                    # print team name

######################## Heaps #########################################################################################

def minHeapBuild(teamArray, maxSize):                                       # assemble min heap
    index = maxSize                                                         # set index to maxSize
    while (index >=0):                                                      # while index is greater than 0
        minHeapify(teamArray,maxSize, index)                                # recursively go through teamArray
        index -= 1                                                          # move down the array

def minHeapify(teamArray, maxSize, index):                                  # minHeapify
    left = leftChild(index)                                                 # index of the left child
    right = rightChild(index)                                               # index of the right child
    min = index                                                             # set min to index

    if(left <= maxSize and teamArray[left].year < teamArray[min].year):     # if left is less than maxsize and min
        min = left                                                          # left becomes min
    if(right <= maxSize and teamArray[right].year < teamArray[min].year):   # if right is less than maxSize and min
        min = right                                                         # right becomes min
    if(min != index):                                                       # if min is not equal to index
        swap(teamArray, index, min)                                         # swap teams
        minHeapify(teamArray, maxSize, min)                                 # heapify

def minHeap(teamArray, length):                                             # minHeap
    maxSize = length - 1                                                    # set maxSize
    minHeapBuild(teamArray, maxSize)                                        # build the minHeap
    index = maxSize                                                         # set index to maxsize
    while index > 0:                                                        # while index is greater than 0
        swap(teamArray, 0, index)                                           # swap teams
        index -= 1                                                          # work down array
        minHeapify(teamArray, index, 0)                                     # heapify

def swap(teamArray, i, j):                                                  # swap
    temp = teamArray[i]                                                     # set temp equal to i
    teamArray[i] = teamArray[j]                                             # set i equal to j
    teamArray[j] = temp                                                     # set j equal to temp

def parent(index):                                                          # get parent index
    return (index - 1)/2

def leftChild(index):                                                       # get index of left child
    return 2 * index + 1

def rightChild(index):                                                      # get index of right child
    return 2 * index + 2

def printTeams(teamArray, length):                                          # printTeams
    for items in teamArray:
        print(items.team)
    print("\n")
######################## Main ##########################################################################################

# team objects
eagles = Team("Philadelphia Eagles", 1933)
bears = Team("Chicago Bears", 1920)
packers = Team("Green Bay Packers", 1921)
cowboys = Team("Dallas Cowboys", 1960)
redskins = Team("Washington Redskins", 1932)
vikings = Team("Minnesota Vikings", 1961)
panthers = Team("Carolina Panthers", 1995)
giants = Team("New York Giants", 1925)
colts = Team("Indianapolis Colts", 1953)
dolphins = Team("Miami Dolphins", 1966)

# new array to hold team objects
newArray = []

newArray.append(colts)
newArray.append(giants)
newArray.append(vikings)
newArray.append(dolphins)
newArray.append(eagles)
newArray.append(bears )
newArray.append(packers)
newArray.append(panthers)
newArray.append(cowboys)
newArray.append(redskins)


length = len(newArray)
minHeap(newArray, length)

# copy heap to new array
copiedArray = [0 for i in range(length)]
print("\n")
for i in range(length):
    copiedArray[i] = newArray[length - i - 1]

# print sorted array
printTeams(copiedArray,length)
