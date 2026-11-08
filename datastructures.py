from collections import deque #THIS is the library used to implement queue data structure...we will use deque data structure to implement queue datastructures 
#class for implementing stack and its operations
class Stack:
    #initialises a stack data structure...initialises a list to implement stack data structures
    def __init__(self):
        self.items=[]
    #it is a function to add an element into stack
    def push(self,value):
        
        self.items.append(value)
        print(value,"added to stack!!")
    #it is a methhod used to delete or pop an element from stack.I deletes the top element of the stack..
    def pop(self):
        if len(self.items)==0:
            print("Stack is Empty(Stack Underflow..)")
        else:
            removed=self.items.pop()
            print("Removed element:",removed)
    #this mehod return the top element of the stack
    def peek(self):
        if len(self.items)==0:
            print("Stack is Empty!!")#stack empty denotes stack underflow error
        else:
            print("Top element:",self.items[-1])
    #this function is to display the stack elements
    def display(self):
        if len(self.items)==0:
            print("Stack is Empty!")
        else:
            print("\n----------STACK----------")
            for item in reversed(self.items):
                print("|",item,"|")

#thsi class uswd to store queue implementation methods
class Queue:
    #initialises a dequeue to  implement queue operations
    def __init__(self):
        self.items=deque()
    #it adds element into tyhe queue from rear..
    def enqueue(self,value):
        self.items.append(value)
        print(value, "adfded into the queue")
    #this operation is used to delete an element bfrom queue. it deletes  element from front
    def dequeue(self):
        if len(self.items)==0:
            print("Queue is Empty!")
        else:
            removed=self.items.popleft()
            print("Removed Element:",removed)
    #this is a queue operation which returns front element of tthe queue
    def front(self):
        if len(self.items)==0:
            print("Queue is Empty!")
        else:
            print("Front Element: ",self.items[0])
    #this function is used to display tye queue
    def display(self):
        if len(self.items)==0:
            print("Queue is Empty!")
        else:
            print("\n FRONT -> ",list(self.items),"<- REAR")

#CLASS USED FOR IMPLEMENTING LINKEDLIST
#class to create a node with data and the next to store the address of the next data
class Node:
    #initialises a new node for new data: value is stored in data, adn next stores the 'none' initially
    def __init__(self,val):
        self.data=val
        self.next=None
#class for linkedlist operations
class LinkedList:
    #initialises starting node as head
    def __init__(self):
        self.head=None
    #this functiuon add an element at the becginning of the list
    def insert_at_beg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        print(data, "inserted at beginning..")
    #this function adds an element at the end of the list
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head= newnode
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=newnode
        print(data, "inserted at end...")
    #this method is used to delete a particular element from the list
    def delete(self,value):
        if self.head is None:
            print("Linked list is empty..")
            return 
        if self.head.data==value:
            self.head=self.head.next
            print(value,"deleted!!")
        current=self.head
        while current.next is not None:
            if current.next.data == value:
                current.next=current.next.next
                print(value, "Deleted!!")
            current=current.next
        print("Element not found!!")
    #this function is used to search a particular element in the list
    def search(self,val):
        current=self.head
        pos=1
        while current is not None:
            if current.data==value:
                print("Element found at position:",pos)
            current=current.next
            pos+=1
        print("Elemnt not found!")
    #used to display the list
    def display(self):
        if self.head is None:
            print("LinkedList is empty...")
            return
        current=self.head
        print("HEAD -> ",end=" ")
        while current is not None:
            print(current.data,end="-> ")   
            current=current.next
        print("None")         
#IMPLEMENTING STACKS USING LINKEDLISTS
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LLStack:
    #initialises the top elemnet of the stack as top
    #this shows that we are implementing stack operations
    def __init__(self):
        self.head=None
    #push operation is to add an element into stack from the top of the stack
    def push(self,data):
        print(data,"inserted into the stack")
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        print(data,"inserted into the stack")
    def peek(self):
        print(self.head.data," peek element of the stack")
    #pop element deletes the element from the stack
    def pop(self):
        print(self.head.data,"popped from the stack")        
        self.head=self.head.next
    #to display the stack 
    def display(self):
        curr=self.head
        while curr!=None:
            print("|",curr.data,"|")
            curr=curr.next
#IMPLEMENTING QUEUES USING LINKEDLISTS
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LLQueue:
    def __init__(self):
        self.head=None
    def enqueue(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
        print(val,"inserted into queue")
    def dequeue(self):
        print(self.head.data,"deleted from queue")
        self.head=self.head.next 
    def front(self):
        print(self.head.data,"is the front of the queue") 
    def rear(self):
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        print(curr.data,"is the rear of the queue")
    def display(self):
        curr=self.head
        print("Front->")
        while curr!=None:   
            print(curr.data,"->")
            curr=curr.next
        print("<- rear")       
#Main program
cho=input("enter stack or queue or linkedlists:")#takes input from user
#to implement stack enter input as 'stack'
if cho=="stack":
    my_stack=Stack()
    while True:
        print("\n=======ALGO PLAY=======")
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Display")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:#add element into stack
            value=int(input("enter your value: "))
            my_stack.push(value)
        elif choice==2:#pop an element from stack
            my_stack.pop()
        elif choice==3:#return the top element of thge stack
            my_stack.peek()
        elif choice==4:#display the stack elements
            my_stack.display()
        elif choice==5:#exit
            print("Thank you for using algo play!!..")
            break
        else:#for in valid input
            print("Invalid choice!Try again....")
#to implement Queues
elif cho=="queue":
    my_queue=Queue()
    while True:
        print("\n=======ALGO PLAY=======")
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Front")
        print("4.Display")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:#adds and element into the queue
            value=int(input("enter your value: "))
            my_queue.enqueue(value)
        elif choice==2:#deletes an element from queue
            my_queue.dequeue()
        elif choice==3:#returns the front element 
            my_queue.front()
        elif choice==4:#displays queue
            my_queue.display()
        elif choice==5:
            print("Thank you for using algo play!!..")
            break
        else:
            print("Invalid choice!Try again....")
#to implement linkedlists----------------------------
elif cho=="linkedlist":
    my_list=LinkedList()
    while True:
        print("\n=======ALGO PLAY=======")
        print("1.insert at beg")
        print("2.insert at end")
        print("3.delete")
        print("4.search")
        print("5.display")
        print("6.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            value=int(input("enter your value: "))
            my_list.insert_at_beg(value)
        elif choice==2:
            value=int(input("enter your value: "))
            my_list.insert_at_end(value)
        elif choice==3:
            val=int(input("enter a value to delete:"))
            my_list.delete(val)
        elif choice==4:
            my_list.display()
        elif choice==6:
            print("Thank you for using algo play!!..")
            break
        elif choice==5:
            val=int(input("enter element to search: "))
            my_list.search(val)
        else:
            print("Invalid choice!Try again....")
#to implement stacks using linked lists
elif cho=="stackll":
    my_list_stack=LLStack()
    while True:
        print("\n=======ALGO PLAY=======")
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.peek")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            value=int(input("enter your value: "))
            my_list_stack.push(value)
        
        elif choice==2:
            my_list_stack.pop()
        elif choice==3:
            my_list_stack.display()
        elif choice==4:
            my_list_stack.peek()
        elif choice==5:
            print("Thank you for using algo play!!..")
            break
        else:
            print("enter valid input!!")
else:
    my_list_queue=LLQueue()
    while True:
        print("\n=======ALGO PLAY=======")
        print("1.ENQUEUE")
        print("2.DEQUEUE")
        print("3.FRONT")
        print("4.REAR")
        print("5.DISPLAY")
        print("6.EXIT")
        choice=int(input("Enter your choice:"))
        if choice==1:
            value=int(input("enter your value: "))
            my_list_queue.enqueue(value)
        
        elif choice==2:
            my_list_queue.dequeue()
        elif choice==3:
            my_list_queue.front()
        elif choice==4:
            my_list_queue.rear()
        elif choice==6:
            print("Thank you for using algo play!!..")
            break
        elif choice==5:
            my_list_queue.display()
        else:
            print("enter valid input!!")
