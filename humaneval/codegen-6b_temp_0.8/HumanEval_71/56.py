
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
    # In Python, the value of True is 1 and False is 0.
    # We need to convert True to 1 and False to 0.
    if a + b > c and a + c > b and a + c > b:
        if a == b == c:
            return 'This is a equilateral triangle'
        elif a == b or a == c or b == c:
            return 'This is a isosceles triangle'
        else:
            return 'This is a scalene triangle'
    return -1
