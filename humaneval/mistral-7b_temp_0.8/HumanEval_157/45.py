
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
    # Check if a,b and c are integers
    if not(a, b, c).is_integer():
        return False
    # Check if a,b, and c are positive
    if not(a, b, c).is_positive():
        return False
    # Check if the sum of any two sides is greater than the third
    if a + b > c and a + c > b and b + c > a:
        # Check if the third side squared is less than the sum of the other two sides squared
        if c * c <= a * a + b * b:
            return True
        else:
            return False
    else:
        return False
