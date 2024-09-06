def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the squares of the lengths of the sides
    side_squares = [a*a, b*b, c*c]
    # Calculate the Pythagorean sum of the sides
    sum_of_squares = side_squares[0] + side_squares[1] + side_squares[2]
    # Check if a right-angled triangle is formed
    return sum_of_squares == 2*side_lengths[0]