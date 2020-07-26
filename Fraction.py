from math import gcd, ceil, floor
class Frac:
    def __init__(self, *fraction):
        if len(fraction) == 1:
            if type(fraction[0]) == float:
                st = str(fraction[0])
                afterPoint = len(st) - st.index(".") - 1
                denominator = 10 ** afterPoint
                numerator = fraction[0] * denominator
            
            elif type(fraction[0]) == int:
                numerator = fraction[0]
                denominator = 1
                
            elif type(fraction[0]) == str:
                st = str(fraction[0])
                numerator = int(st[:st.index("/")])
                denominator = int(st[st.index("/")+1:])
            
        elif len(fraction) == 2 and type(fraction[0]) == type(fraction[1]) == int:
            numerator = fraction[0]
            denominator = fraction[1]
            
        if denominator < 0:
            numerator *= -1
            denominator *= -1
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

    def __bool__(self):
        if self.numerator == 0:
            return False
        else:
            return True

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
        if power < 0:
            power *= -1
            denominatorP = self.numerator ** power
            numeratorP = self.denominator ** power
        elif power == 0:
            denominatorP = 1
            numeratorP = self.numerator
        else:
            denominatorP = self.denominator ** power
            numeratorP = self.numerator ** power
        return Frac(numeratorP, denominatorP)
    
    def floor(self):
        return floor(self.numerator / self.denominator)
    
    def ceil(self):
        return ceil(self.numerator / self.denominator)
    
    def cut(self):
        return int(self.numerator / self.denominator)
    
    def simplify(self):
        denominatorS = self.denominator // gcd(self.numerator, self.denominator)
        numeratorS = self.numerator // gcd(self.numerator, self.denominator)
        return Frac(numeratorS, denominatorS)
    
    def reverse(self):
        denominatorR = self.numerator
        numeratorR = self.denominator
        return Frac(numeratorR, denominatorR)
    
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
        self.numerator = numeratorA
        return self
        
    def __isub__(self, second):
        denominatorS = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorS = (denominatorS // self.denominator) * self.numerator - (denominatorS // second.denominator) * second.numerator
        self.denominator = denominatorS
        self.numerator = numeratorS
        return self
        
    def __imul__(self, second):
        denominatorM = self.denominator * second.denominator
        numeratorM = self.numerator * second.numerator
        self.denominator = denominatorM
        self.numerator = numeratorM
        return self
    
    def __idiv__(self, second):
        denominatorD = self.denominator * second.numerator
        numeratorD = self.numerator * second.denominator
        self.denominator = denominatorD
        self.numerator = numeratorD
        return self
    
    def __ipow__(self, power):
        denominatorP = self.denominator ** power
        numeratorP = self.numerator ** power
        self.denominator = denominatorP
        self.numerator = numeratorP
        return self
