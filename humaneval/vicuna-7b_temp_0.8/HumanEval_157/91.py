
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
    # check if any of the side is zero or negative
    if a < 0 or b < 0 or c < 0:
        return False
    
    # check if all three side are equal
    if a == b == c:
        return True
    
    # calculate the longest side
    if a != b and a != c:
        if a + b > c:
            b = a + c - b
        elif b + c > a:
            c = b + a - c
        else:
            a = b + c - a
    
    # check if the longest side is the hypotenuse
    if a == c:
        return True
    
    # check if the remaining two side is equal or ratio is 1:1
    if b == a or c == b or a == c:
        return True
    
    # if all condition fails
    return False
