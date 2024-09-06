
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
    def is_right_angle(a, b, c):
        # Calculate the cosine of the angle between the two shorter sides
        cos_angle = (b**2 + c**2 - a**2) / (2 * a * np.sqrt(1 - (b**2 + c**2)/a**2))

        # Check if the cosine of the angle is zero
        if cos_angle == 0:
            return False

        # Check if the cosine of the angle is negative
        if cos_angle < 0:
            return False

        return True

    return is_right_angle(a, b, c)
