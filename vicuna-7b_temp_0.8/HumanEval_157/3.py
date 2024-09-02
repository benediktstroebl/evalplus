
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
    # check if two sides are equal
    if a == b:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if a + b == c:
        return True
    # check if two sides are equal
    if b == c:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if a + c == b:
        return True
    # check if two sides are equal
    if c == a:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if b + a == c:
        return True
    # check if two sides are equal
    if a == b + c:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if b + c == a:
        return True
    # check if two sides are equal
    if b == c + a:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if c + a == b:
        return True
    # check if two sides are equal
    if a == b + c + a:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if b + c + a == a:
        return True
    # check if two sides are equal
    if c + b == a + c + b:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if a + c + b == b + a + c:
        return True
    # check if two sides are equal
    if b + c + a == a + b + c:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if a + b + c + b == a + b + c:
        return True
    # check if two sides are equal
    if b + c == a + b + a + c:
        return True
    # check if hypotenuse is equal to sum of other two sides
    if a + b + c + b == a + b + c + b:
        return True
    return False
