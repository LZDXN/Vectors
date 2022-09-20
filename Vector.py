class Vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        self.figure = '.5'
        
    def __repr__(self):
        return f'<{self.i}, {self.j}, {self.k}>'

    def __str__(self):
        return f'<{self.i}, {self.j}, {self.k}>'
    
    def __copy__(self):
        return Vector(self.i, self.j, self.k)
    
    def changeFigure(self, figure):
        self.figure = '.%sg' % figure
        return self
    
    def formating(self, value):
        return float(format(value, self.figure))
    
    def __add__(self, other):
        i = self.formating(self.i + other.i)
        j = self.formating(self.j + other.j)
        k = self.formating(self.k + other.k)
        return Vector(i, j, k)

    def __sub__(self, other):
        i = self.formating(self.i - other.i)
        j = self.formating(self.j - other.j)
        k = self.formating(self.k - other.k)
        return Vector(i, j, k)

    def __iadd__(self, other):
        i = self.formating(self.i + other.i)
        j = self.formating(self.j + other.j)
        k = self.formating(self.k + other.k)
        return Vector(i, j, k)

    def __isub__(self, other):
        i = self.formating(self.i - other.i)
        j = self.formating(self.j - other.j)
        k = self.formating(self.k - other.k)
        return Vector(i, j, k)
    
    def __mul__(self, scalar): # times scalar
        i = self.formating(self.i * scalar)
        j = self.formating(self.j * scalar)
        k = self.formating(self.k * scalar)
        return Vector(i, j, k)
    
    def __truediv__(self, scalar): # dvided scalar
        i = self.formating(self.i / scalar)
        j = self.formating(self.j / scalar)
        k = self.formating(self.k / scalar)
        return Vector(i, j, k)
    
    def __imul__(self, scalar): # times scalar
        i = self.formating(self.i * scalar)
        j = self.formating(self.j * scalar)
        k = self.formating(self.k * scalar)
        return Vector(i, j, k)
    
    def __itruediv__(self, scalar): # dvided scalar
        i = self.formating(self.i / scalar)
        j = self.formating(self.j / scalar)
        k = self.formating(self.k / scalar)
        return Vector(i, j, k)
    
    def dotProduct(self, other):
        i = self.formating(self.i * other.i)
        j = self.formating(self.j * other.j)
        k = self.formating(self.k * other.k)
        return Vector(i, j, k)
    
    def crossProduct(self, other):
        i = self.formating(self.j * other.k - self.k * other.j)
        j = self.formating(-(self.i * other.k - self.k * other.i))
        k = self.formating(self.i * other.j - self.j * other.i)
        return Vector(i, j, k)
    
    def magnitude(self):
        return self.formating((self.i ** 2 + self.j ** 2 + self.k ** 2) ** (1 / 2))
    
    def unit(self): # for unit vector
        return self.__truediv__(self.magnitude())
    
    # projection, theta
        