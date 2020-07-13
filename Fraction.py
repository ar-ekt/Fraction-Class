from math import gcd
class Frac:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.floated = numerator / denominator
        
    def __repr__(self):
        return "%d/%d" % (self.numerator, self.denominator)    
    
    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Frac(-self.numerator, self.denominator)
    
    def __add__(self, second):
        denominatorA = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorA = (denominatorA // self.denominator) * self.numerator + (denominatorA // second.denominator) * second.numerator
        return Frac(numeratorA, denominatorA)
    
    def __sub__(self, second):
        denominatorS = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorS = (denominatorS // self.denominator) * self.numerator - (denominatorS // second.denominator) * second.numerator
        return Frac(numeratorS, denominatorS)
    
    def __mul__(self, second):
        denominatorM = self.denominator * second.denominator
        numeratorM = self.numerator * second.numerator
        return Frac(numeratorM, denominatorM)
    
    def __truediv__(self, second):
        denominatorD = self.denominator * second.numerator
        numeratorD = self.numerator * second.denominator
        return Frac(numeratorD, denominatorD)
    
    def __pow__(self, power):
        denominatorP = self.denominator ** power
        numeratorP = self.numerator ** power
        return Frac(numeratorP, denominatorP)
    
    def __lt__(self, second):
        return self.floated < second.floated
    def __gt__(self, second):
        return self.floated > second.floated
    def __le__(self, second):
        return self.floated <= second.floated
    def __ge__(self, second):
        return self.floated >= second.floated
    def __eq__(self, second):
        return self.floated == second.floated
    def __ne__(self, second):
        return self.floated != second.floated
    
    def __iadd__(self, second):
        denominatorA = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorA = (denominatorA // self.denominator) * self.numerator + (denominatorA // second.denominator) * second.numerator
        self.denominator = denominatorA
        self.denominator = numeratorA
        return self
        
    def __isub__(self, second):
        denominatorS = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorS = (denominatorS // self.denominator) * self.numerator - (denominatorS // second.denominator) * second.numerator
        self.denominator = denominatorS
        self.denominator = numeratorS
        return self
        
    def __imul__(self, second):
        denominatorM = self.denominator * second.denominator
        numeratorM = self.numerator * second.numerator
        self.denominator = denominatorM
        self.denominator = numeratorM
        return self
    
    def __idiv__(self, second):
        denominatorD = self.denominator * second.numerator
        numeratorD = self.numerator * second.denominator
        self.denominator = denominatorD
        self.denominator = numeratorD
        return self
    
    def __ipow__(self, power):
        denominatorP = self.denominator ** power
        numeratorP = self.numerator ** power
        self.denominator = denominatorP
        self.denominator = numeratorP
        return self
    
    def floor(self):
        return self.numerator // self.denominator
