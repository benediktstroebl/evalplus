def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter s of the triangle
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return (s * (s - a) == b * c) or (s * (s - b) == a * c) or (s * (s - c) == a * b)