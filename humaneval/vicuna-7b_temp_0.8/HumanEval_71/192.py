
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
    x1, x2, x3 = a, b, c
    if x1 + x2 > x3 or x2 + x3 > x1 or x3 + x1 > x2:
        return -1
    return (x1 * x2 * x3) / (2 * a)
