def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle's right angle
    s = (a ** 2 + b ** 2) ** 0.5
    t = (a ** 2 + c ** 2) ** 0.5

    # Check if the length of the sides form a right-angled triangle
    return s == t or s == c or t == c