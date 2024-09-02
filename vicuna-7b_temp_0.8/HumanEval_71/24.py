
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
    if (a + b + c) < a or (a + b + c) < b or (a + b + c) < c:
        return -1
    if a < b < c:
        return (a * b * (c - b)) / (3 * (c - a))
    elif b < c < a:
        return (b * c * (a - c)) / (3 * (a - b))
    else:
        return (c * (a - b) * (b - c)) / (3 * (a - c))
