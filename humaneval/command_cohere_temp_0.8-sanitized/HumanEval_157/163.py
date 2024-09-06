def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter s of the triangle

    # Check if the triangle is a right-angled triangle
    if s * (s - a) == b * c:
        return True
    else:
        return False