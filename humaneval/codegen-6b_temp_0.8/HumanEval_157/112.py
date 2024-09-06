
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
    x = math.pow(a, 2) + math.pow(b, 2)
    y = math.pow(b, 2) + math.pow(c, 2)
    z = math.pow(c, 2) + math.pow(a, 2)
    if x == y or y == z or z == x:
        return True
    return False
