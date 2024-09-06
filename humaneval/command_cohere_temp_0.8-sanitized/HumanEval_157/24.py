def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the sine of the angle opposite each side
    sin_opposite = [sin(math.acos(b / a)) if a != 0 else None,
                     sin(math.acos(c / b)) if b != 0 else None,
                     sin(math.acos(a / c)) if c != 0 else None]
    # Check if any of the sines are equal to 1/sqrt(2)
    return any(x == 1 / math.sqrt(2) for x in sin_opposite)