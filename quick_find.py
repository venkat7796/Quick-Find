class quick_find(object):
    def __init__(self,n):
        self.arr = [0] * n
        for i in range(n):
            self.arr[i] = i
    
    def connected(self,p,q):
        if self.arr[p] == self.arr[q]:
            return True
        else:
            return False
    
    def union(self,p,q):
        id1 = self.arr[p]
        id2 = self.arr[q]
        for i in range(len(self.arr)):
            if self.arr[i] == id1:
                self.arr[i] = id2
    
    def print_arr(self):
        print(self.arr)

c = quick_find(10)
c.union(4,3)
c.union(3,8)
c.union(6,5)
c.union(9,4)
c.union(2,1)
print(c.connected(8,9))
print(c.connected(5,0))
c.union(5,0)
c.union(7,2)
c.union(6,1)
c.print_arr()
