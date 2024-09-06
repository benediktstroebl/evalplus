
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
    # Calculate the cosine of the angle between the two shorter sides
    c1 = (b**2 + a**2 - c**2) / (2 * a * b)
    # If the cosine is greater than 0, the angle is less than 90 degrees
    if c1 > 0:
        return False
    # If the cosine is less than or equal to 0, the angle is greater than 90 degrees
    else:
        return True
