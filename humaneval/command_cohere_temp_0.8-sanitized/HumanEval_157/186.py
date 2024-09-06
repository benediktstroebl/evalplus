def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the squares of the lengths of the sides
    side_squares = [a**2, b**2, c**2]

    # Check if the sum of the squares of the two shorter sides is equal to the square of the longest side
    if side_squares[0] + side_squares[1] == side_squares[2]:
        return True
    else:
        return False