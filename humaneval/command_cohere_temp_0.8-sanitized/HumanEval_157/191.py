def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    r = sqrt(s * (s - a) * (s - b) * (s - c))  # Hypotenuse radius

    # Verify if the triangle is right-angled
    return r == abs(a - b) or r == abs(a - c) or r == abs(b - c)