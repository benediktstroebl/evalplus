
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
    # choose the one with the largest side
    if a >= b:
        if b >= c:
            a, b, c = b, c, a
    else:
        if c >= b:
            a, b, c = c, a, b
    # if both the sides are equal equal
    if a == b and b == c:
        return True
    # if any two sides are smaller than the third
    if a < b or b < c:
        return False
    # if the third side is right angle
    return (b**2 + c**2) == a**2
    