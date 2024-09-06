
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
    
    ab = math.sqrt(pow(a, 2) + pow(b, 2))
    ac = math.sqrt(pow(a, 2) + pow(c, 2))
    bc = math.sqrt(pow(b, 2) + pow(c, 2))
    
    if ab == ac and ab == bc:
        return True
    
    return
