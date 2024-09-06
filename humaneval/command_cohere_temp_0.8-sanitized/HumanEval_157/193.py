def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of a right angle triangle
    s = (a ** 2 + b ** 2) ** 0.5
    t = (a ** 2 + c ** 2) ** 0.5

    # Check if the length of the third side is the hypotenuse of a right angle
    return s == t