
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
    if math.fabs(math.fabs(a - b) - math.fabs(a - c)) == 0:
        if math.fabs(a - b) == c or math.fabs(a - c) == b or math.fabs(a - b) == c:
            return True
    return
