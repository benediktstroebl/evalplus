
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
    if (a >= b + c) or (a <= 0) or (b >= c + a) or (b <= 0) or (c >= b + a) or (c <= 0):
        return -1
    return round(0.5 * ((a + b + c) * (-1 + 2 * (a + b + c))), 2)

