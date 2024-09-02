
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
    # Check if two sides are equal
    if a == b:
        return False

    # Calculate the length of the hypotenuse
    c = sqrt(a**2 + b**2)

    # Check if the other two sides are both less than the hypotenuse
    if a < c and b < c:
        return True

    # Check if the length of the hypotenuse is equal to the longest side
    if a == c:
        return True

    # Check if the length of the hypotenuse is equal to the smallest side
    if b == c:
        return True

    # If none of the above conditions are met, the triangle is not right-angled
    return False
