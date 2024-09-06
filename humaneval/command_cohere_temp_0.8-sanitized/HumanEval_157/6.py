def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    
    # Determine if the triangle is right-angled
    if hypotenuse == c or hypotenuse == abs(a - c) or hypotenuse == abs(b - c):
        return True
    else:
        return False