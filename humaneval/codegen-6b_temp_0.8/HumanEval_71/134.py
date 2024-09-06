
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
    # Don't change the indentation of the if statement, just rewrite it.
    # Check if the three sides of the given triangle is a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Then calculate the area of the triangle
        a = math.hypot(b,c)
        area = 0.25 * (a * (a + b + c))
        return round(area, 2)
    else:
        return -1
