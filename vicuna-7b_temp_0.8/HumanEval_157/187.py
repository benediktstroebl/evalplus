
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
    # Check if the lengths of all sides are positive integers
    if (a < 0) or (b < 0) or (c < 0) or (a < 0) or (b < 0) or (c < 0):
        return False
    # Check if the length of the hypotenuse is equal to the sum of the other two sides
    if a + b != c:
        return False
    # Return True if the above conditions are met
    return True
