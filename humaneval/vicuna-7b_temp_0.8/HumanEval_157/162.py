
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
    # check if all the three sides are positive integers
    if not all(map(int, [a, b, c])):
        return False

    # check if the longest side is equal to the sum of the other two sides
    if abs(b - a) != abs(c - a):
        return False

    # if the above two conditions are met, it is a right-angled triangle
    return True
