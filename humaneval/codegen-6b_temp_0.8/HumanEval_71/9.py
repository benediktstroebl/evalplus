
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
    if a > b and a > c:
        a, b, c = b, a, c
    elif b > a and b > c:
        b, a, c = a, b, c
    elif c > a and c > b:
        c, a, b = a, b, c

    if a >= b + c:
        return -1
    return round((a * b * c) / 2.0, 2)