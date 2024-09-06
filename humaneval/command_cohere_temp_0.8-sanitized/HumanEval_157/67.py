def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the square of each length
    squares = [a**2, b**2, c**2]
    # Calculate the cross product
    cross = squares[0] * squares[1] - squares[2] * sides[1] * sides[2]
    # Determine if the triangle is right-angled
    if cross > 0:
        return True
    else:
        return False