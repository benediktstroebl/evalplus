
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

    # Calculate the longest side
    if a != b and a != c:
        long_side = max(a, b, c)
    else:
        long_side = a

    # Calculate the angle between the longest side and the side that is not
    # longest
    if long_side == a:
        acos = math.acos(c / b)
    else:
        acos = math.acos(b / a)

    # Calculate the angle between the longest side and the hypotenuse
    if b == long_side:
        angle_between_longest_side_and_hypotenuse = math.pi / 2
    else:
        angle_between_longest_side_and_hypotenuse = math.atan(b / long_side)

    # Check if the angle between the longest side and the hypotenuse is a right angle
    if angle_between_longest_side_and_hypotenuse == math.pi / 2:
        return True

    # Check if the angle between the longest side and the hypotenuse is less than 
    # 180 degrees
    if angle_between_longest_side_and_hypotenuse < math.pi / 2:
        return False

    # If none of the above conditions are met, the triangle is not right-angled
    return False
