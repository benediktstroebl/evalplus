def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine the difference between the largest two sides and the third side
    sides = sorted([a, b, c])
    diff = sides[1] - sides[0]
    # Determine if the sides form a right-angled triangle
    return abs(diff) <= s / 2  # noqa: W150