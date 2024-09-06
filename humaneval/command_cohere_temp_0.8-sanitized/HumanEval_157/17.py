def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # semi-perimeter
    # Check if the triangle is right-angled
    if s * (s - a) ** 2 + s * (s - b) ** 2 + s * (s - c) ** 2 == 0:
        return True
    else:
        return False