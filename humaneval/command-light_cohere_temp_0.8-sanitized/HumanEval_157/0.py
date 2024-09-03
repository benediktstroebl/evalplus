def right_angle_triangle(a, b, c):
    '''
    Check if a triangle with sides of lengths a, b, c has a right angle
    Returns: Boolean indicating whether the triangle is right-angled or not
    '''
    return (a == b and b == c) and a > 90