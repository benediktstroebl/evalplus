
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
    sides = [a, b, c]
    angles = set()
    for side in sides:
        if side < 0:
            return False
        else:
            angles.add(math.degrees(math.acos(side/math.sqrt(side**2+side**2))))
    return len(angles) == 1 and (90 in angles or math.isclose(180, max(angles))
