def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2) ** 0.5
    
    # Check if the length of the hypotenuse is equal to c and return true if so
    return hypotenuse == c