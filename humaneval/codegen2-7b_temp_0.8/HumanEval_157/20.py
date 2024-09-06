
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
    angle1 = radians(math.acos(a/c)*180/math.pi)
    angle2 = radians(math.acos(b/c)*180/math.pi)
    angle3 = radians(math.acos(c/a)*180/math.pi)
    if abs(angle1 - angle2) < 0.0001 and abs(angle2 - angle3) < 0.0001:
        return True
    else:
        return
