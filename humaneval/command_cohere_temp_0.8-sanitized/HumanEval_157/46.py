def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the squared length of the hypotenuse
    hypotenuse_squared = (a ** 2 + b ** 2 + c ** 2) ** 0.5
    # Check if the sum of the two shorter sides is equal to the squared hypotenuse
    return hypotenuse_squared == (side_lengths[0] ** 2 + side_lengths[1] ** 2)