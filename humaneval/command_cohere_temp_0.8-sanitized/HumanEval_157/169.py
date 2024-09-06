def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle sides
    s = (a + b + c) / 2  # Semiperimeter
    x = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Length of the fourth side

    return x ** 2 == a * b or x ** 2 == b * c or x ** 2 == c * a