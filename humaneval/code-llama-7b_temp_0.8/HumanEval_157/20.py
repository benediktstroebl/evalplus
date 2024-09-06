
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
    # code goes here
    x = int(a)
    y = int(b)
    z = int(c)
    if x == y == z:
        return True
    elif (x == z and y == z) or (x == y and z == y) or (x == y and z == x) or (y == z and x == z):
        return True
    else:
        return False
