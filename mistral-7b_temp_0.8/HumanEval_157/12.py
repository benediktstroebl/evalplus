
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
    # First, we have to find out the smallest value
    # Since the smallest value is the base of the triangle, the smallest value will always be less than or equal to the other two values
    # So, if any of the values is bigger than the other two, the values are not a right-angled triangle.

    if a > b or a > c:
        return False
    elif b > a or b > c:
        return False
    elif c > a or c > b:
        return False

    # So, we will not be able to find a right-angled triangle from the given values if we get to this part
    if a**2 + b**2 == c**2:
        return True

    # Now, we will check if the values form a triangle with a right angle
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        return False

    # If none of the conditions above are met, it means that the values form a triangle with a right angle.
    return True
