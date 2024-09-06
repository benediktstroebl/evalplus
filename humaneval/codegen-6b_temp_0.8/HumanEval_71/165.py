
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
    
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        area = round(area, 2)
        return area
    else:
        return -1

assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(1, 2, 10) == -1
assert triangle_area(10, 5, 15) == 10.00
assert triangle_area(10, 3.3, 15) == 10.00
assert triangle_area(11, -2, 11) == -1
assert triangle_area(10, 10, 10) == -1
assert triangle_area(10, 10, 9) == -1
assert triangle_area(1, 5, 7) == -1