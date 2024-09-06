
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
    a_b = a + b
    b_c = b + c
    c_a = c + a
    if a_b > b_c and a_b > c_a:
        return a * b / 2
    elif b_c > a_b and b_c > c_a:
        return b * c / 2
    elif c_a > a_b and c_a > b_c:
        return c * a / 2
    else:
        return -1
