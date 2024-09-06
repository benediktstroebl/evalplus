
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
    s1 = a + b
    s2 = b + c
    s3 = a + c
    if a > 0 and b > 0 and c > 0 and s1 < s2 + s3 and s1 > 0:
        return round((s1 * (s2 - s3) * 0.5), 2)
    else:
        return -
