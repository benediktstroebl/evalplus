
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

    # if all sides are greater than 0 return the area
    if a > 0 and b > 0 and c > 0:
        return (a + b + c) / 2.0
    # check if the three sides form a valid triangle
    elif a + b + c == 6:
        return (a + b) / 2.0
    # if the sides sum is less than 6 return -1
    else:
        return -1
