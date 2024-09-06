
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
    # Check if the three sides make a valid triangle
    if (a + b + c) / 2 < max(a, b, c):
        return round(3.141592653589793238462643383279502884197169399375105820974944592307816406286208994459) * (min(a, b, c) / 2) ** 2, 2)
    else:
        return -1
