def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    d = (a**2 + b**2)**0.5
    e = (b**2 + c**2)**0.5

    # Check for right angle
    return (d**2 + e**2 == a**2 + b**2) and (d**2 + e**2 == b**2 + c**2)