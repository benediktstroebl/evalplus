
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
    # Use the Pythagorean theorum to solve for the hypotenuse
    # and the three sides
    c_ = (a * a + b * b) ** 0.5
    side_1 = (b * b + c * c) ** 0.5
    side_2 = (c * c + a * a) ** 0.5
    if c_ == side_1 or c_ == side_2 or c_ == b:
        return True
    else:
        return False
