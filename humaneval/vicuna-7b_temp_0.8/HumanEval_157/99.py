
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
    angle1 = math.radians(30)
    angle2 = math.radians(120 - 30)
    hypotenuse = math.sqrt(a**2 + b**2 + c**2)
    
    if c**2 == (a**2 + b**2):
        return False
    elif (angle2 - angle1) * hypotenuse == c:
        return True
    else:
        return False
