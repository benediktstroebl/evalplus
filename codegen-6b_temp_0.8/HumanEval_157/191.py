
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
    # Hint: use the half of the angle formula.
    # Use the from_triangle function to convert triangle lengths to sides.
    # The from_triangle function returns a list of sides.
    # (a, b, c) = from_triangle(a, b, c)
    # return is_right_angle(a, b, c)
    #return is_right_angle(from_triangle(a, b, c)[1], from_triangle(a, b, c)[2], from_triangle(a, b, c)[3])
    return is_right_angle(a, b, c, from_triangle(a, b, c))
