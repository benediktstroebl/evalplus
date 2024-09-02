
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
    if a == b and b == c:
        return True
    elif (a == b and b!= c) or (b == c and c!= a) or (a == c and c!= b):
        return False
    else:
        return right_angle_triangle(a, b, c-1) or right_angle_triangle(a, b-1, c) or right_angle_triangle(a-1, b, c
