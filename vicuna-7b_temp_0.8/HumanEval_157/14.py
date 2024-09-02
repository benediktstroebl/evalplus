
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
    # if all sides are equal
    if a == b and b == c:
        return True

    # if all sides are 0 or 1
    if a == 0 or b == 0 or c == 0:
        return True

    # find the longest side
    if a > b and a > c:
        longest_side = a
    elif b > c and b > a:
        longest_side = b
    else:
        longest_side = c

    # if the longest side is odd
    if longest_side % 2 != 0:
        # if all sides are odd or even
        if (b % 2 == 0 and c % 2 == 0) or (b % 2 == 1 and c % 2 == 1):
            return True
        else:
            return False
    else:
        # if all sides are even or odd
        if (b % 2 == 0 and c % 2 == 0) or (b % 2 == 1 and c % 2 == 1):
            return True
        else:
            return False
