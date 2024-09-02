
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
    s1 = a + b + c
    s2 = a + b - c
    s3 = a - b + c
    s4 = a - b - c

    if (s1 == s2) and (s2 == s3) and (s3 == s4):
        return True
    else:
        return False
