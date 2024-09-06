def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return (s * (s - a) == b ** 2) or (s * (s - b) == a ** 2) or (s * (s - c) == c ** 2)