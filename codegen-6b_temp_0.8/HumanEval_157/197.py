
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
    # set the values for any side
    sides = [a, b, c]
    
    # process the values to evaluate the angles
    for i in xrange(3):
        sides[i] = float(sides[i])
        
    # check if the sides are right angled
    if a == b and a == c:
        return False
    elif a == b or a == c:
        return False
    elif b == c or b == a:
        return False
    elif c == a or c == b:
        return False
    
    # if all of the angles are right angled, return True
    return True
