
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
    if ((a + b) + c) > a:
        halfway = (a + b) / 2
        area = 0.5 * (a * (halfway + c))
    elif ((a + c) + b) > c:
        halfway = (b + c) / 2
        area = 0.5 * (b * (halfway + a))
    elif ((b + a) + c) > a:
        halfway = (c + a) / 2
        area = 0.5 * (c * (halfway + b))
    elif (a + b) + c > 13:
        return -1
    else:
        return 0
    
