
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
    # If you can't sum any two sides then your triangle is invalid
    if a+b <= c or a+c <= b or b+c <= a:
        return -1
    
    # If triangle sides are valid then there exists a, b, c such that a+b+c = side_lengths
    # Therefore sum of any two sides = c where c is valid
    # return 0.5 * a * b / 2 + 0.5 * a * c / 2 + 0.5 * b * c / 2
    return 0.5 * (a + b + c)
