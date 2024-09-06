def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse ** 2 == a ** 2 + b ** 2