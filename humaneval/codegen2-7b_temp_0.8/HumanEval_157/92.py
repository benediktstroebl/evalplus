
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
    if a+b < c or b+c < a or c+a < b:
        return False
    elif abs(a-b) == c:
        return True
    elif abs(b-c) == a:
        return True
    elif abs(c-a) == b:
        return True
    else:
        return False
