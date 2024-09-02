
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
    # Check if any sides are equal to zero
    if (a == 0 or b == 0 or c == 0):
        raise ValueError("The lengths of any side cannot be zero!")
    # Check if all three sides are equal
    if (a == b and b == c):
        return True
    # Check if the third side is the hypotenuse
    elif (c > a + b):
        return False
    # Otherwise it is a right angle triangle
    else:
        return True