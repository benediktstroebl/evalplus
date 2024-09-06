
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
    
    # Check if the three sides are all greater or equal to 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check if any two sides are equal or not
    elif a == b == c:
        return True
    
    elif a == b or b == c or c == a:
        return True
    
    else:
        return False
    
