def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of a right triangle
    s = (a**2 + b**2 + c**2)**0.5
    p = (a**2 + c**2 - b**2)**0.5

    # Determine if the triangle is right angled
    if s**2 + p**2 == c**2:
        return True
    else:
        return False