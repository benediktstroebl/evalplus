def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle
    s = (a**2 + b**2 + c**2) / 2
    as_b = math.sqrt(s * (s - a) * (s - b))
    return abs(as_b - c) < 1e-6