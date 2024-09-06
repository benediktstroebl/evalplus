def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semiperimeter
    p = (a * b * c) ** 0.5  # Perimeter

    # Determine if the triangle is right-angled
    return p * s == 2  # Pythagorean theorem