def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    d = ((a ** 2) + (b ** 2) - (c ** 2)) ** 0.5
    e = ((b ** 2) + (c ** 2) - (a ** 2)) ** 0.5
    # Check for the presence of a right angle
    return d * e == b * c and d + e == c + a