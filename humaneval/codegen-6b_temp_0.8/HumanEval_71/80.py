
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
    side1 = a + b
    side2 = a + c
    side3 = b + c
    if side1 > c:
        if side1 > side2:
            if side2 > side3:
                return round((side1*side2)/2, 2)
            else:
                return -1
        else:
            return -1
    else:
        if side2 > side3:
            if side2 > side1:
                return round((side2*side3)/2, 2)
            else:
                return -1
        else:
            return -1
    return -1
