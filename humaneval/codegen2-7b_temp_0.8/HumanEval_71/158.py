
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
    a_sq = a ** 2
    b_sq = b ** 2
    c_sq = c ** 2
    summation = (a + b + c)
    if a_sq + b_sq > c_sq:
        return summation / 2
    else:
        return -
