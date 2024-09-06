
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
    # TODO: implement this function.

    # if the sum of two sides is greater than the third side
    # then the triangle is valid
    if (a + b) > c and (a + c) > b and (b + c) > a:
        # the area of the triangle is
        triangle_area = (a + b + c) / 4.0
        # we round the area to 2 decimal points
        triangle_area = round(triangle_area, 2)
        return triangle_area

    # if the sum of any two sides is less than the third side
    # then the triangle is not valid
    return -1

