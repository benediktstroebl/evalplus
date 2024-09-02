
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
    # check if sides are in the correct order
    if (b-a)**2 + (c-a)**2 > (a-b)**2:
        # check if sum of two sides is greater than the third side
        if (b-a) + (c-a) > a - b:
            return (a*c)/2
    return -1