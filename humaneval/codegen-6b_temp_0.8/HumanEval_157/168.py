
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
    if a > 0 and b > 0 and c > 0:
        return math.isclose(math.hypot(b, c), a) and \
                (b + c > a) and \
                (b + a > c) and \
                (c + a > b)
    return False
