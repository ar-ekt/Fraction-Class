from math import gcd, ceil, floor, trunc
class Frac:
    def __init__(self, *fraction):
        if len(fraction) == 1:
            if type(fraction[0]) == float:
                st = str(fraction[0])
                afterPoint = len(st) - st.index(".") - 1
                denominator = 10 ** afterPoint
                numerator = int(fraction[0] * denominator)
            
            elif type(fraction[0]) == int:
                numerator = fraction[0]
                denominator = 1
                
            elif type(fraction[0]) == str:
                st = fraction[0]
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
    
    def __int__(self):
        return int(self.floated)
    
    def __float__(self):
        return self.floated
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Frac(-self.numerator, self.denominator)
    
    def __abs__(self):
        return Frac(abs(self.numerator), self.denominator)

    def __floor__(self):
        return floor(self.floated)
    
    def __ceil__(self):
        return ceil(self.floated)
    
    def __round__(self):
        return round(self.floated)
    
    def __trunc__(self):
        return trunc(self.floated)
    
    def __bool__(self):
        if self.numerator == 0:
            return False
        else:
            return True

    def __add__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        denominatorA = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorA = (denominatorA // self.denominator) * self.numerator + (denominatorA // second.denominator) * second.numerator
        return Frac(numeratorA, denominatorA)
    
    def __sub__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        denominatorS = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorS = (denominatorS // self.denominator) * self.numerator - (denominatorS // second.denominator) * second.numerator
        return Frac(numeratorS, denominatorS)
    
    def __mul__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        denominatorM = self.denominator * second.denominator
        numeratorM = self.numerator * second.numerator
        return Frac(numeratorM, denominatorM)
    
    def __truediv__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        denominatorD = self.denominator * second.numerator
        numeratorD = self.numerator * second.denominator
        return Frac(numeratorD, denominatorD)
    
    def __floordiv__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return floor(self.floated // second.floated)
    
    def __mod__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        denominatorM = (self.denominator * second.denominator) // gcd(self.denominator, second.denominator)
        numeratorM = ((denominatorM // self.denominator) * self.numerator) % ((denominatorM // second.denominator) * second.numerator)
        return Frac(numeratorM, denominatorM)
    
    def __pow__(self, power):
        if power < 0:
            power *= -1
            denominatorP = self.numerator ** power
            numeratorP = self.denominator ** power
        elif power == 0:
            return 1
        else:
            denominatorP = self.denominator ** power
            numeratorP = self.numerator ** power
        return Frac(numeratorP, denominatorP)
    
    __iadd__ = __add__
    __isub__ = __sub__
    __idiv__ = __truediv__
    __imul__ = __mul__
    __ifloordiv__ = __floordiv__
    __imod__ = __mod__
    __ipow__ = __pow__
    
    def __lt__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated < second.floated
    
    def __gt__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated > second.floated
    
    def __le__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated <= second.floated
    
    def __ge__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated >= second.floated
    
    def __eq__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated == second.floated
    
    def __ne__(self, second):
        if type(second) != Frac:
            second = Frac(second)
        return self.floated != second.floated
    
    def simplify(self):
        denominatorS = self.denominator // gcd(self.numerator, self.denominator)
        numeratorS = self.numerator // gcd(self.numerator, self.denominator)
        return Frac(numeratorS, denominatorS)
    
    def reverse(self):
        denominatorR = self.numerator
        numeratorR = self.denominator
        return Frac(numeratorR, denominatorR)
