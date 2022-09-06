import math
import random
from maths import per
from misc import the

class Num:
    def __init__(self, c = 0 , s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True
    
    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has

    def add(self, v):
        if v!="?":
            self.n = self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the["nums"]:
                self._has.append(v)
            else:
                pos = random.randint(0,len(self._has)-1)
                self.isSorted = False
                self._has[pos] = v

    def div(self):
        return (per (self.nums(),0.9)-per(self.nums(),0.1))/2.58

    def mid(self):
        return per(self.nums(), 0.5)