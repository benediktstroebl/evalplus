
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
    # First, we need to check if the three sides can form a right angle.
    # I have assumed a right angle can't be formed by 3 sides with different lengths
    if (a == b or b == c or a == c):
        return False
    # Now, we check if the right-angle triangle can be formed by these three sides
    # and use heron's formula to find the square root of the hypotenuse.
    # If the square root is less than or equal to 1, we know that the right-angle
    # triangle can't be formed
    if (math.sqrt(a**2 + b**2) >= c):
        return False
    # If the square root is greater than 1, it means that the right-angle
    # triangle can be formed.
    return True
