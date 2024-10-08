
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or c + b < a:
        return False
    if c ** 2 == a ** 2 + b ** 2:
        return True
    elif c ** 2 > a ** 2 + b ** 2:
        return False
    else:
        return True
