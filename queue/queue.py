"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Element:
    def __init__(self,value,next_element=None):
        self.value = value
        self.next_element = next_element
class Queue:
    def __init__(self):
        self.size = 0
        self.head: Element = None
        self.tail: Element = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        if self.tail is None:
            new_el = Element(value,None)
            self.head = new_el
            self.tail = new_el
        else:
            new_tail = Element(value,None)
            old_tail = self.tail
        self.size += 1
    def dequeue(self):        
        if not self.head:
            return None
        if self.head.next_element is None:
            self.size -= 1
            head_val = self.head.value
            self.head = None
            self.tail = None
            return head_val
        self.size -= 1
        head_val = self.head.value
        self.head = self.head.next_element
        return head_val
n = Queue()
n.enqueue(3)
n.enqueue(4)

print(n.tail.value)