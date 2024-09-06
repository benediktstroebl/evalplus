
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
    # Check if c is equal to the hypotenuse
    if c != math.sqrt(a**2 + b**2):
        return False
    
    # Check if the angle between the sides is a right angle
    angle = math.degrees(math.atan2(b, a))
    if angle != math.pi/2:
        return False
    
    return True