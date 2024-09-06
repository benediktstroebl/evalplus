def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Height

    # Verify that the triangle is right-angled
    return h == a or h == b or h == c