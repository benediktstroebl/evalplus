def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or
    90 degrees.
    """
    min_side = min(a, b, c)
    if abs(a - b) <= min_side ** 0.5 or abs(b - c) <= min_side ** 0.5 or abs(c - a) <= min_side ** 0.5:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        else:
            return False
    else:
        return False