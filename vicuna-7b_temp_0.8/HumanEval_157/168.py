
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
    def haversine(p1, p2):
        # https://en.wikipedia.org/wiki/Haversine_formula
        return 2 * math.atan2(math.sqrt(p1[0]**2 + p1[1]**2),
                              math.sqrt(p2[0]**2 + p2[1]**2))

    angle = haversine(a, b) - haversine(b, c)
    if angle == math.pi:
        return True
    return False
