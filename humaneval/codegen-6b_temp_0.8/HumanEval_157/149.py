
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
    test = [a, b, c]
    if a == b and b == c:
        return True
    if a == c and c == b:
        return True
    if a == b and b != c:
        return False
    if a != b and b != c and c != a:
        return False
    if a != b and b == c:
        return False
    if a == c and c != b:
        return False
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return False
    if a < 0:
        return False
    if b < 0:
        return False
    if c < 0:
        return False
    return True
