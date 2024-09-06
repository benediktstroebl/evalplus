def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) / (2 * s)  # Height

    # Check if the triangle is right-angled
    if h == (a * b * c) / (a + b + c):
        return True
    else:
        return False