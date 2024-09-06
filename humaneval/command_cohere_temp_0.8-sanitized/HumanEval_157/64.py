def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) ** 0.5  # Hypotenuse using Heron's formula

    return h == c or h == a or h == b