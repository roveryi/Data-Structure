class LinearList(object):
    def __init__(self, data):
        self.data = data
        self.last = self.length()-1
    @classmethod
    def MakeEmpty(self):
        self.data = []
        self.last = -1

    @classmethod
    def Find(self, target):
        i = 0
        while i < self.length():
            if target != self.data[i]:
                i += 1
            else: return i
        return None

    @classmethod
    def Insert(self, target, position):
        if position > self.length() or position < 0: 
            print('Not possible')
            return None
        temp = self.data[0:position]
        temp.append(target)
        for i in range(position, self.length()):
            temp.append(self.data[i])
        self.data = temp
        self.last += 1

    @classmethod
    def Delete(self, position):
        if position >= self.length() or position < 0: 
            print('Not possible')
            return None
        
        self.data = self.data[0:position]+self.data[position+1:]
        self.last -= 1

    @classmethod
    def length(self):
        return len(self.data)

