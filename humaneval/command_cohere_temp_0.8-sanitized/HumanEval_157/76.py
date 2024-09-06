def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the square of the longest side
    max_side = max(side_lengths)
    long_side_square = max_side * max_side
    # Calculate the sum of the squares of the other two sides
    sum_side_squares = (side_lengths[1] * side_lengths[1]) + (side_lengths[2] * side_lengths[2])
    # Check if the triangle is right-angled
    if long_side_square == sum_side_squares:
        return True
    else:
        return False