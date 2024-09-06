
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
    return round((a + b + c) * (1/2) * (1/2), 2) if a+b > c and a + c > b and b + c > a else -1

assert triangle_area(1, 2, 10) == -1
assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(3, 3, 3) == 1.00
assert triangle_area(3, 4, 3) == 1.5
assert triangle_area(6, 4, 6) == 7.5
assert triangle_area(3, 4, 11) == -1
assert triangle_area(3, 9, 3) == 3.00
assert triangle_area(3, 4, 5) == 6.00
