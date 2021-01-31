class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, data):
        self.val = Node(data[0]).val
        self.next = None
        self.traverse(data)

    def traverse(self,data):
        temp, counter = self, 1
        while counter < len(data):
            temp.next = Node(data[counter])
            temp = temp.next 
            counter += 1
    def length(self):
        temp, counter = self, 0
        while temp:
            counter += 1
            temp = temp.next 
        return counter 

    def insert(self, target, position):
        n = self.length()
        if position < 0 or position > n: 
            print('Invalid Position')
            return None
        temp, counter, new_node =self, 0, Node(target)
        while counter < position:
            temp = temp.next
            counter += 1
        old_next = temp.next 
        new_node.next = old_next 
        temp.next = new_node

    def delete(self, position):
        n = self.length()
        if position < 0 or position > n: 
            print('Invalid Position')
        return None
        temp_pre, counter_pre, counter_cur =self, 0, 0
        temp_cur = temp_pre
        while counter_pre < position-1:
            temp_pre = temp_pre.next 
            counter_pre += 1

        while counter_cur < position:
            temp_cur = temp_cur.next 
            counter_cur += 1
        temp_cur = temp_cur.next 
        temp_pre.next = temp_cur


