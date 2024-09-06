def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Determine if the triangle is right-angled
    if hypotenuse ** 2 == c ** 2 and hypotenuse ** 2 == a ** 2 + b ** 2:
        return True
    else:
        return False