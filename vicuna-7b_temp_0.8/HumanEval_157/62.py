
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    def __str__(self):
        return "A triangle with sides: {} {} {}".format(self.a, self.b, self.c)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __str__(self):
        return "A triangle with sides: {} {} {}".format(self.a, self.b, self.c)

    def angle(self):
        return (90 - (self.b**2 + self.c**2) ** 0.5)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __str__(self):
        return "A triangle with sides: {} {} {}".format(self.a, self.b, self.c)

    def area(self):
        return (self.b * self.c) / 2

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __str__(self):
        return "A triangle with sides: {} {} {}".format(self.a, self.b, self.c)

    def hypotenuse(self):
        return math.sqrt(self.b**2 + self.c**2)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __str__(self):
        return "A triangle with sides: {} {} {}".format(self.a, self.b, self.c)

    def is_right_angle(self):
        return (self.b**2 + self.c**2) ** 0.5 == 90