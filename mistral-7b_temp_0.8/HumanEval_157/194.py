
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
    # Triangle with three equal sides.
    if a == b and a == c:
        return False

    # No triangle with unequal sides.
    if a == b and a != c:
        return False
    if a == c and a != b:
        return False
    if b == c and b != a:
        return False

    # Check that one side is at least as long as the others.
    if a > b and a > c:
        return a ** 2 >= b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 >= a ** 2 + c ** 2
    if c > a and c > b:
        return c ** 2 >= b ** 2 + a ** 2

    # No triangle.
    return False

