
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
    # The cosine of the the right angle
    c_cos = (a**2 + b**2 - c**2) / (2*a*b)
    # If its greater than 1 then the triangle is not a right angle triangle
    return c_cos < 1
