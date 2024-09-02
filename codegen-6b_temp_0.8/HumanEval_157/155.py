
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
    s1 = '3', '4', '5'
    s2 = '3', '4', '12'
    s3 = '1', '2', '3'
    s4 = '1', '2', '12'
    s5 = '1', '2', '3'
    s6 = '1', '1', '2'
    if a != '3' and b != '4' and c != '5':
        return False
    elif a == '3' and b == '12' and c == '5':
        return True
    elif a == '1' and b == '2' and c == '3':
        return True
    elif a == '1' and b == '12' and c == '3':
        return True
    elif a == '1' and b == '2' and c == '12':
        return True
    elif a == '1' and b == '1' and c == '2':
        return True
    else:
        return False
