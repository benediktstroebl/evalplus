
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
    s1 = a + b + c
    s2 = b + c + a
    s3 = c + a + b
    return 0.5 * abs(s1 - s2) * abs(s1 - s3) if s1 > s2 and s1 > s3 else -1

