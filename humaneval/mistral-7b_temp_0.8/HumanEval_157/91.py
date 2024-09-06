
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
    # Hint:
    # In a right-angled triangle, the side opposite the right angle is called the 
    # hypotenuse. In a right-angled triangle, the square of the hypotenuse is 
    # equal to the sum of the squares of the other two sides.

    # Hint:
    # Use the math.sqrt() function to calculate the square root of a number.
    # Make use of the fact that all sides of a right-angled triangle are
    # greater than or equal to zero.
    # This function may use the built-in functions math.hypot() and math.sqrt().
    a_squared = a**2
    b_squared = b**2
    c_squared = c**2
    h_squared = a_squared + b_squared

    if h_squared == c_squared:
        return True
    else:
        return False

