class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.next=None
    
class LinkedList:
    def __init__(self, next=None) -> None:
        self.head = None
        self.count = 0

    def is_empty(self) :
        return self.count == 0

    def addFirst(self, value) :
        node = Node(value)
        if not self.is_empty() : 
            node.next = self.head
            self.head = node
        else : self.head = node
        self.count =+ 1

    def addLast(self, value) :
        node = Node(value)
        if self.head == None : 
            self.head = node
            self.count =+ 1
            return
        copy = self.head 
        while copy != None : 
            if copy.next == None :
                break
            copy = copy.next
        copy.next = node
        self.count =+ 1
        self = copy

    def getLastElement(self):
        if self.is_empty() : return None
        copy = self.head
        while copy != None :
            if copy.next == None:
                break
            copy = copy.next
        return copy.value
    
    def getFirstElement(self):
        if not self.is_empty() : return self.head.value
        else : return None


    def display(self) :
        copy = self.head
        print("[", end="")
        while copy != None : 
            print(copy.value, end="-> ")
            copy = copy.next
            self.count += 1
        print("X]")

if __name__ == "__main__" :
    lchainee = LinkedList()
    lchainee.addLast(3)
    print(lchainee.is_empty())
    print(lchainee.getLastElement())


