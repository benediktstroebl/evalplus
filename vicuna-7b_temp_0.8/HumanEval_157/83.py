
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
    # Check if any two sides are equal
    if a == b or a == c or b == c:
        return False
    
    # Calculate the longest side
    if a + b > c:
        longest_side = a + b
    else:
        longest_side = c
    
    # Calculate the other two sides
    if longest_side == 0:
        return False
    else:
        c = longest_side / 2
    
    # Check if the triangle is right-angled
    if c * c == longest_side:
        return True
    else:
        return False
