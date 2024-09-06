def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semiperimeter
    d = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Diameter
    r = d / 2  # Radius

    # Verify if the triangle is right-angled
    return r == a or r == b or r == c