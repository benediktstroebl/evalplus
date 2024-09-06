
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
    # Check if all sides are equal
    if a != b and a != c and b != c:
        return False
    
    # Check if hypotenuse is twice the longest side
    if a*a + b*b != c*c:
        return False
    
    # Check if angle opposite the longest side is a right angle
    if a == max(a, b, c):
        return True
    
    # If none of the above conditions met, it's not a right angle triangle
    return False
