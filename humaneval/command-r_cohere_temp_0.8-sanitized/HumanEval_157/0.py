def right_angle_triangle(a, b, c):
    '''
    Checks if the three sides form a right angle triangle.
    '''
    return a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2