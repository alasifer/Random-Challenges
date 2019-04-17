
'''
Given a string A consisting of n characters and a string B consisting of m characters, 
write a function that will return the number of times A must be stated such that B is a substring of the repeated A. 
If B can never be a substring, return -1.

Example:
A = ‘abcd’
B = ‘cdabcdab’

Refrence for the porblem: https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/

'''
class Node:
    def __init__(self, item=None):
        self.data = item
        self.next = None
        self.visit = False

class LinkedList:

    def __init__(self):
        self.head = Node()
        self.last = None
        self.lastIter = None

    def insert(self, val, circule=False):
        '''
        This method insert item to the list based on the end of the linked list.
        if small is true it will make a circular linked list, where the last item points to the head
        '''
        if self.head.data == None:
            self.head.data = val
            self.last = self.head
            return
        else:
            curr = self.last
            curr.next = Node(val)
            if circule:
                curr.next.next = self.head
            self.last = curr.next

    def find(self, value, trace=True):
        '''
        this method finds the item based on its value. 
        if trace is True that means whichever item is found for the first time, we will skip it if 
        we are looking for the same item but at the next position
        '''
        curr = self.head
        if curr.data == value:
            curr.visit = True
            return curr

        elif trace:
            while curr.next is not None:
                if curr.next.data == value and not curr.next.visit:
                    curr.next.visit = True
                    return curr.next
                curr = curr.next 

        else:
            while curr.next is not None:
                if curr.next.data == value:
                    return curr.next
                curr = curr.next  
            

           
def numberOfTimes(listA, listB):  

    string = LinkedList()
    origin = LinkedList()

    for char in listB:
        string.insert(char)

    for char in listA:
        origin.insert(char,True)

    counter = 0
    ch = 0
    for j in range(len(listB)-1):
        B = string.find(listB[j])
        A = origin.find(listB[j], False)
        ch += 1
        if B.next.data == listA[-1]:
            counter += 1
            ch = 0
        if B.next.data != A.next.data:
            return -1
    
    if ch > 0:
        counter += 1

    #result = listA*counter
    return counter






        
