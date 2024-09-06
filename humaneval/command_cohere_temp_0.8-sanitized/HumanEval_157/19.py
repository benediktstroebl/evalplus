def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) / (2 * s)  # Height

    # Check if the height is equal to the half of the longest side
    return h == b / 2 or h == c / 2 or h == a / 2