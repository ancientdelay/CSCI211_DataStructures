#########################################################
#                                                       #
#   Seamus Gosman                                       #
#   CIS 211                                             #
#   Spring 2020                                         #
#   Assignment 8                                        #
#                                                       #
#########################################################

######################## Node Class ####################################################################################
class Team:                                             # team class
    def __init__(self, team, year):                     # initializer
        self.height = 1
        self.left = None                                # set left to None
        self.right = None                               # set right to None
        self.year = year                                # set year
        self.team = team                                # set team

    def getName(self):                                  # get name
        return self.team                                # return team name

    def getYear(self):                                  # get year
        return self.year                                # return team year

    def getHeight(self):                                # get height
        return self.height                              # return height

    def printTeam(self):                                # print team
        print(self.team)                                # print team name

######################## Tree Class ####################################################################################
class AVLTree:
    def __init__(self):                                         # constructor
        self.root = None                                        # set avl tree root to none

    def insert(self, root, team):                               # insert team node into AVL tree
        if not root:                                            # root = None
            return team                                         # return team
        elif (team.year < root.year):                           # else if team.year is less than root nodes year
            root.left = self.insert(root.left, team)            # enter into left branch
        else:                                                   # else
            root.right = self.insert(root.right, team)          # enter into right branch
        # set height

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)                         # set balance

        if balance > 1 and team.year < root.left.year:          # if balance is greater than and team < root
            return self.rotateRight(root)                       # rotate right
        elif balance < -1 and team.year > root.right.year:      # if balance is less than -1 and team > root
            return self.rotateLeft(root)                        # rotate left
        elif balance > 1 and team.year > root.left.year:        # if balance is greater than 1 and team > root
            root.left = self.rotateLeft(root.left)              # root left = rotate left root left
            return self.rotateRight(root)                       # return rotate right
        elif balance < -1 and team.year < root.right.year:      # else if balance is less than -1 and team < root
            root.right = self.rotateRight(root.right)           # right = rotate right
            return self.rotateLeft(root)                        # return rotate left
        return root                                             # return root

    def rotateLeft(self, team):                                 # rotate left
        n = team.right                                          # n = team to be rotated
        t1 = n.left                                             # t1 = node to rotate with

        n.left = team                                           # set n to left
        team.right = t1                                         # set right to t1

        # adjust heights
        team.height = 1 + max(self.getHeight(team.left), self.getHeight(team.right))
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right))

        return n                                                # return n

    def rotateRight(self, team):                                # rotate right
        n = team.left                                           # n = left
        t2 = n.right                                            # t2 = right

        n.right = team                                          # set right to team
        team.left = t2                                          # set left to t2
                                                                # adjust heights

        # adjust heights
        team.height = 1 + max(self.getHeight(team.left), self.getHeight(team.right))
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right))

        return n                                                # return n

    def getHeight(self, root):                                  # get height of node
        if root == None:                                        # if root is empty
            return 0                                            # height = 0
        return root.height                                      # return height

    def getBalance(self, root):                                 # get balance
        if root == None:                                        # if root is empty
            return 0                                            # return 0

        return self.getHeight(root.left) - self.getHeight(root.right)   # return left height minus right height

    def inOrder(self, node):                                            # print in order, using recursion
        if (node == None):                                              # if node is empty
            return                                                      # return
        else:                                                           # if node is not empty
            self.inOrder(node.left)                                     # use method on left branch
            node.printTeam()                                            # print team name
            self.inOrder(node.right)                                    # use method on right branch

    def breadthOrder(self, root):                                       # print in breadth order
        if root is None:                                                # if root is empty
            return
        queue = []                                                      # queue for teams
        queue.append(root)                                              # add root to queue

        while queue:                                                    # while queue is true
            count = len(queue)                                          # set count equal to length of queue
            while count > 0:                                            # while count is less than 0
                temp = queue.pop(0)                                     # pop team off of queue
                print(temp.team, "" , end = "")                         # print team
                if temp.left:                                           # if left is not empty
                    queue.append(temp.left)                             # append to queue
                if temp.right:                                          # if right is not empty
                    queue.append(temp.right)                            # append to queue
                count -= 1                                              # reduce count by one
            print('')

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

# new AVL tree
newTree = AVLTree()

root = newTree.root

root = newTree.insert(root, bears)
root = newTree.insert(root, packers)
root = newTree.insert(root, giants)
root = newTree.insert(root, redskins)
root = newTree.insert(root, eagles)
root = newTree.insert(root, colts)
root = newTree.insert(root, cowboys)
root = newTree.insert(root, vikings)
root = newTree.insert(root, dolphins)
root = newTree.insert(root, panthers)

# level order
print("\n### Breadth Order ###\n")
newTree.breadthOrder(root)
