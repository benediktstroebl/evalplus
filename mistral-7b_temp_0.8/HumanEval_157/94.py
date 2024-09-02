
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
    # find the square of a
    a2 = a * a
    # find the square of b
    b2 = b * b
    # find the square of c
    c2 = c * c
    # find the sum of a2 + b2
    sum = a2 + b2
    # find the difference of c2 - sum
    diff = c2 - sum
    # check if diff is 0
    if diff == 0:
        return True
    # if diff is not 0, return False
    return False
