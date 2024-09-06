
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
    # Checks types
    if type(a) != int or type(b) != int or type(c) != int:
        return -1
    if a < 0 or b < 0 or c < 0:
        return -1

    # Checks if we can make a triangle
    if a < (b + c) and b < (a + c) and c < (b + a):
        return round(float((a + b + c) * (float(a) / 2) * (float(c) / 2)), 2)
    return -1

