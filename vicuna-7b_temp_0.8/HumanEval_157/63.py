
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
    if a == b or b == c or c == a:
        return False
    
    # Calculate the length of the third side
    if b != 0 and c != 0:
        x = (a**2 + b**2 - c**2) / (2*a*b)
    else:
        x = 0
    
    # Return True if the length of the third side is equal to the hypotenuse
    return x == c
