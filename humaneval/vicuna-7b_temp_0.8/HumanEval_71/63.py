
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # A right angled triangle can be defined by the condition a^2 + b^2 - c^2 = 0
    if (a**2 + b**2 - c**2) == 0:
        # In a right angled triangle, the length of the hypotenuse is c
        hypotenuse = c
        # The other two sides are a and b
        a = c / hypotenuse
        b = c / hypotenuse
        return (a*b) * hypotenuse**2
    elif (a*b) < c**2:
        return -1
    else:
        # Otherwise, the triangle is not a right angled triangle
        return None