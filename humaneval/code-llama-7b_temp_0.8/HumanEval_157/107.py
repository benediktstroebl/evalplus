
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
    # find the longest side
    if a >= b and a >= c:
        longest_side = a
        if longest_side * 2 > b + c:
            return True
        else:
            return False
    elif b >= a and b >= c:
        longest_side = b
        if longest_side * 2 > a + c:
            return True
        else:
            return False
    else:
        longest_side = c
        if longest_side * 2 > b + a:
            return True
        else:
            return False
