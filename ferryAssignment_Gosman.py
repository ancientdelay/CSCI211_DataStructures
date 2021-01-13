############################################
#                                          #
#   Seamus Gosman                          #
#   CIS 211                                #
#   Spring 2020                            #
#   Lab Assignment 5                       #
#                                          #
############################################

################ Car Class ###########################################################################################

class Car:

    count = 0                                                   # count for class method

    @classmethod                                                # method to generate ID numbers
    def nextIDNum(self):
        self.count += 1
        return self.count

    def __init__(self):
        self.carID = Car.nextIDNum()                            # set ID Num to next number
        self.description = "Car ID: " + str(self.carID)         # print car description

################ Queue Class ###########################################################################################

class Queue:

    # array based queue
    def __init__(self):                                         # initializer
       self.maxSize = 20                                        # max size of queue
       self.queue = []                                          # array based queue
       self.size = 0                                            # size of queue

    def enqueue(self, newCar):                                  # add to queue
        if(self.isFull() != True):                              # if queue is not full
            self.queue.append(newCar)                           # add car
            self.size += 1                                      # size + 1
        else:                                                   # else
            print("* Queue Is Full *")                              # alert users

    def dequeue(self):                                          # remove from queue
        if(self.isEmpty() == False):                            # if queue is not empty
            self.queue.pop()                                          # remove
            self.size -= 1                                      # size minus 1
        else:                                                   # else
            print("* Queue Is Empty *")                             # alert user

    def isFull(self):                                           # boolean is full
        return self.size == self.maxSize                        # if size = maxsize

    def isEmpty(self):                                          # boolean is empty
        return self.size == 0                                   # return true if size = 0

    def printQueue(self):                                       # print queue
        for cars in self.queue:                                 # for loop
            print(cars.description)                             # print description

################ Program  ##############################################################################################

def runProgram():
    print("\n\t\t\"On The Way To Cape May...\"")
    laneArray = [] * 5                                          # array to hold lanes

    Lane1 = Queue()                                             # lanes
    Lane2 = Queue()
    Lane3 = Queue()
    Lane4 = Queue()
    Lane5 = Queue()

    laneArray.append(Lane1)                                     # add lanes to lane array
    laneArray.append(Lane2)
    laneArray.append(Lane3)
    laneArray.append(Lane4)
    laneArray.append(Lane5)

    on = True                                                   # boolean for program loop
    while(on == True):                                          # while on
                                                                # menu
        print('''                                               
        #############################################
        #               Commands                    #
        #############################################
        #                                           #
        # Add : Add Cars                            #
        #                                           #
        # Load: Start Boarding Process              #
        #                                           #
        # Exit : Exit Program                       #
        #                                           #
        #############################################
                ''')


        command = input("\tPlease Enter A Command: ")         # enter command
                                                                # if statements for commands
        if (command.lower() == "add"):                          # add cars
            add(laneArray)
        elif (command.lower() == "load"):                       # load boat
            load(laneArray)
        elif (command.lower() == "exit"):                       # exit program
            exitProgram()
        else:                                                   # if input is invalid
            print("\t* Error: Invalid Input *")                       # print error message

def add(laneArray):                                             # add lane, takes in lane array

    carCount = 0                                                # set car count to 0
    numOfCarsLoaded = [int] * 5                                 # array to tally number of cars loaded into each lane
    i = 0                                                       # set i to 0
                                                                # set each value in the array to 0
    while(i < len(numOfCarsLoaded)):                            # while i is less than length of array
        numOfCarsLoaded[i] = 0                                  # set value to 0
        i += 1                                                  # go to next place in array

    laneCount = 0                                                          # lane count set to 0
    count = 0                                                              # count set to 0
    numOfCars = int(input("\n\tHow Many Cars Would You Like To Add: "))  # ask user to input num of cars
    print("")
    while(count < numOfCars and laneCount <= 4):                           # while count is less than input and
                                                                           # lanes are available
        if(laneArray[laneCount].isFull() == False):                        # if lane is not full
            newCar = Car()                                                 # create new car
            laneArray[laneCount].enqueue(newCar)                           # add new car to queue
            count += 1                                                     # count + 1
            carCount += 1                                                  # car count + 1
            numOfCarsLoaded[laneCount] = carCount                          # save num of cars loaded in lane
        elif(laneArray[laneCount].isFull() == True):                       # if lane is full
            laneCount += 1                                                 # set to next lane
            carCount = 0                                                   # reset car count
        else:                                                              # else
            print("\tOut Of Space")                                      # out of space
            totalCar = count + 1                                           # total cars loaded
            carsDenied = numOfCars - totalCar                              # total cars denied
            print("\tTotal Of " + totalCar + " Cars Loaded ")            # print results for cars loaded
            print("\t" + carsDenied + " Cars Unable To Fit")             # print results for cars unable to fit

    laneNum = 1                                                                       # set lane name to 1
    for i in range(laneCount+1):                                                      # loop through lanes
        if(laneNum <= 5):                                                             # if lane are available
                                                                                      # print results
            print("\t" + str(numOfCarsLoaded[i]) + " Cars Loaded Into Lane " + str(laneNum))
            laneNum += 1                                                              # go to next lane
        else:                                                                         # else if no more room
            print("\n\t* Out of space *\n")                                         # alert user
            totalCar = count                                                          # total number of cars loaded
            carsDenied = numOfCars - totalCar                                         # cars unable to fit
            print("\tTotal Of " + str(totalCar) + " Cars Created ")                 # print results for cars loaded
            print("\t" + str(carsDenied) + " Cars Unable To Fit")                   # print results for cars denied
    return laneArray                                                                  # return array of lanes

def load(laneArray):
    count = 0                                                      # set count to 0
    laneCount = 0                                                  # set lane count to 0
    carCount = 0                                                   # set car count to 0
    numOfCarsLoaded = [int] * 5                                    # array to tally number of cars loaded into each lane
    i = 0                                                          # set i to 0

                                                                   # set each value in the array to 0
    while (i < len(numOfCarsLoaded)):                              # while i is less than length of array
        numOfCarsLoaded[i] = 0                                     # set value to 0
        i += 1                                                     # go to next place in array

    while(count < 50 and laneCount < 5):
        if (laneArray[laneCount].isEmpty() == False):              # if lane is not full
            laneArray[laneCount].dequeue()                         # add new car to queue
            count += 1                                             # count + 1
            carCount += 1                                          # car count + 1
            numOfCarsLoaded[laneCount] = carCount                  # save num of cars loaded in lane
        elif (laneArray[laneCount].isEmpty() == True):             # if lane is full
            laneCount += 1                                         # set to next lane
            carCount = 0                                           # reset car count

    print("")
    laneNum = 1  # set lane name to 1
    for i in range(laneCount + 1):                                                                 # loop through lanes
        if (laneNum <= 5):                                                                         # if lane available
            print("\t" + str(numOfCarsLoaded[i]) + " Cars Removed From Lane " + str(laneNum))  # print results
            laneNum += 1                                                                           # go to next lane

def exitProgram():                                                                                 # exit program
    exit(0)

################ main()  ###############################################################################################

runProgram()
