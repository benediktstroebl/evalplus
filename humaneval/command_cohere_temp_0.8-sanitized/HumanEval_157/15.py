def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine the difference between the largest two sides and the third side
    diffuser = max(a, b) - c
    # Determine the square of the diffuser
    diffuser_square = diffuser ** 2
    # Calculate the square of the semi-perimeter
    s_square = s ** 2
    # Return True if the diffuser is less than the semi-perimeter and their
    # squares have equal magnitude
    return diffuser_square <= s_square