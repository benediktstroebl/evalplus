
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
    if a < 1 or b < 1 or c < 1:
        return False
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    return abs(a**2 + b**2 - c**2) < 0.001 or abs(a**2 + c**2 - b**2) < 0.001 or abs(b**2 + c**2 - a**2) < 0.001

