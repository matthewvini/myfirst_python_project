class fractions:
    """ denoting fractions using OOPS concepts"""
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def frac(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den+otherfraction.num*self.den
        newden = self.den * otherfraction.den
        return fractions(newnum,newden)

myfraction1 = fractions(3,4)
myfraction1.frac()
myfraction2 = fractions(4,5)
myfraction2.frac()
print('I ate',myfraction1,'of the pizza.last month i ate',myfraction1+myfraction2)
print(myfraction1+myfraction2)
