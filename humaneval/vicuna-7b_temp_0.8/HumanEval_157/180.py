
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
    # Use Heron's formula to calculate the area of the triangle
    area = (a + b + c) / 2 * (a + b + c) // 2
    
    # If the three sides are equal, the triangle is a square and can't be a
    # right-angled triangle
    if area == 0:
        return False
    
    # Calculate the longest side
    longest_side = max(a, b, c)
    
    # Check if the other two sides are equal to the longest side
    if (b == c and b == longest_side) or (c == a and c == longest_side) or (a == b and a == longest_side):
        return True
    
    # If the three sides are not equal, they are not a right-angled triangle
    return False