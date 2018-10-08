# LAB10.py


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        self.next = new_next

    def __str__(self):
        return "{}".format(self.value)

    __repr__ = __str__


class Stack:

    def __init__(self):
        self.top = None  # Do NOT modify this line
        self.count = 0

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    def push(self, item):
        new_item = Node(item)
        new_item.setNext(self.top)
        self.top = new_item
        self.count += 1

    def pop(self):
        popped_value = self.top.getValue()
        next_item = self.top.getNext()
        del self.top
        self.top = next_item
        self.count -= 1
        return popped_value

    def peek(self):
        return self.top.value

    def printStack(self):
        temp = self.top
        while temp:
            print(temp.getValue())
            temp = temp.getNext()


# Collaboration Statement:
# I worked on the homework(lab) assignment alone, using only previous and current course materials.

