class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        self.add=self.a+self.b
    def substraction(self):
        self.sub=self.a-self.b
    def multiplication(self):
        self.mul=self.a*self.b
    def division(self):
        self.div=self.a/self.b
    def show(self):
        print(self.add)
        print(self.sub)
        print(self.mul)
        print(self.div)
z=calculator(100,10)
z.addition()
z.substraction()
z.multiplication()
z.division()
z.show()