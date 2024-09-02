
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

    # check if three sides form a valid triangle
    if (a + b > c) and (b + c > a) and (c + a > b):
        # calculate the area of the triangle
        if b**2 + c**2 == a**2:
            # isosceles triangle
            if b == c:
                # equilateral triangle
                return a * (sqrt(2) / 2)
            else:
                # isosceles triangle
                return 2 * a * (sqrt(2) / 4)
        else:
            # regular triangle
            return (a * (c / 2)) + (b * sqrt(5)) + (c * (a / 2))
    else:
        return -1
