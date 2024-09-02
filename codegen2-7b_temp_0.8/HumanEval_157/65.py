
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
    angles = []
    if a == b and b == c:
        angles.append(90)
    elif a == b or b == c or a == c:
        angles.append(a)
    elif a == b or a == c or b == c:
        angles.append(b)
        angles.append(c)
    angles.sort()
    return angles[0] == angles[1] and angles[1] ==
