
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
    # Convert all sides to radians
    a = np.radians(a)
    b = np.radians(b)
    c = np.radians(c)
    
    # Calculate the length of the hypotenuse
    c = np.sqrt(a**2 + b**2)
    
    # Check if the triangle is right-angled
    if c**2 < (a**2 + b**2):
        return False
    else:
        return True
