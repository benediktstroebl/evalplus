
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
    angle = np.rad2deg(np.arccos(np.real(a**2 + b**2 + c**2 - 2*a*b*np.cos(np.rad2deg(np.arcsin(c/np.sqrt(a**2 + b**2)))))))
    if angle == np.pi/2:
        return True
    else:
        return False
