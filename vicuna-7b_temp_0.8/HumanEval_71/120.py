
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
    if a + b > c:
        half_b = (b + c) / 2
        if a**2 + half_b**2 > c**2:
            return (a*half_b) / 2.0
        else:
            return -1
    elif b + c > a:
        half_a = (a + b) / 2
        if b**2 + half_a**2 > c**2:
            return (b*half_a) / 2.0
        else:
            return -1
    elif c + a > b:
        half_b = (b + c) / 2
        if c**2 + half_b**2 > a**2:
            return (c*half_b) / 2.0
        else:
            return -1
    else:
        return -1