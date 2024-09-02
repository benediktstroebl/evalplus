
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
    # Check if all the sides are positive integers
    if not all(map(int, [a, b, c])):
        return False
    
    # Check if the triangle is right-angled
    return all(map(lambda x: x >= a, [b, c]))
