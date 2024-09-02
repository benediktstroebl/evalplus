
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

    # make sure that the sum of any two sides is greater than the third side
    if (a + b) > c or (b + c) > a or (c + a) > b:
        return -1
    
    # calculate the area
    if a >= b >= c:
        area = (a + b + c) / 6
    elif b >= a >= c:
        area = (b + a + c) / 6
    else:
        area = (c + b + a) / 6
        
    # round the area to 2 decimal places
    return round(area, 2)
