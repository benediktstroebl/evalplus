
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
    # Use the basic law of cosine to check if one side is right angle
    c_c = (a**2 + b**2 - c**2)/(2*a*b)
    c_c = math.acos(c_c)
    c_c = math.degrees(c_c)
    # The denominator of the law of cosines is the square of the side
    if (a*a + b*b - c*c)**0.5 == 0 or (a*a + c*c - b*b)**0.5 == 0 or \
        (b*b + c*c - a*a)**0.5 == 0:
        return False

    else:
        return True

