
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
    # Hint: use a,b,c to simplify the formula for right angle triangle
    return math.fabs(float(a**2 + b**2 - c**2) / 2 * a) == float(b**2 + c**2 - a**2) / 2 * b == float(c**2 + a**2 - b**2) / 2 * c == float(a**2 + b**2 - c**2) / (2 * a)

