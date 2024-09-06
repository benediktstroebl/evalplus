
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
    a_sq = a**2
    b_sq = b**2
    c_sq = c**2
    cond_1 = c_sq >= a_sq + b_sq
    cond_2 = b_sq >= a_sq + c_sq
    cond_3 = a_sq >= b_sq + c_sq
    return cond_1 and cond_2 and cond_3
