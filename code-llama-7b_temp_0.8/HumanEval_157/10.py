
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
    # Simple solutions
    return a**2 + b**2 == c**2 # return  True if a**2 + b**2 == c**2 else False
    return (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2)
    return (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)

    # Taking modulus of each side
    a_mod, b_mod, c_mod = a % 1, b % 1, c % 1
    if a_mod == 0 or b_mod == 0 or c_mod == 0:
        return False
    else:
        return (a_mod + b_mod == c_mod) or (b_mod + c_mod == a_mod) or (c_mod + a_mod == b_mod)

    # Conditions to check
    conditions = (a**2 + b**2 == c**2, b**2 + c**2 == a**2, c**2 + a**2 == b**2)
    # If any of the condition is True return True else False
    return any(conditions)
