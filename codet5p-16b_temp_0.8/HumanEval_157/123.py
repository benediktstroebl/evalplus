
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

    assert isinstance(a, int), 'The lengths of the sides of a triangle must be integers.'
    assert isinstance(b, int), 'The lengths of the sides of a triangle must be integers.'
    assert isinstance(c, int), 'The lengths of the sides of a triangle must be integers.'
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True

