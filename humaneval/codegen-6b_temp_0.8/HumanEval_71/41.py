
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
    side1 = a
    side2 = b
    side3 = c
    if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side1 + side2):
        return -1
    else:
        return round((side1 * side2 * 1.0 / 2.0), 2) 
