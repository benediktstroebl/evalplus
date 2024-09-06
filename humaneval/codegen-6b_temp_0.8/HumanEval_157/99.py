
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
    import math
    s1 = math.sqrt(b ** 2 + c ** 2)
    s2 = math.sqrt(a ** 2 + b ** 2)
    s3 = math.sqrt(c ** 2 + a ** 2)
    if s1 / s2 == s3 / s2 or s2 / s3 == s3 / s1:
        return True
    return False
