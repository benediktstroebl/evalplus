
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
    if (a + b > c):
        result = (a + b + c) / 2
        area = (result * result) / 4
    elif (a + c > b):
        result = (b + c + a) / 2
        area = (result * result) / 4
    elif (b + c > a):
        result = (a + b + c) / 2
        area = (result * result) / 4
    else:
        area = -1
    return area
