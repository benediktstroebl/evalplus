
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
    if a < 0 or b < 0 or c < 0:
        return -1
    if a == b and b == c:
        return round(sqrt(3) / 2 * (a ** 2), 2)
    elif a != b and a != c and b != c:
        return -1
    else:
        return round((a + b + c) / 2 * sqrt(abs(a * (a + b) * (a + b + c) * (b - c))), 2)

