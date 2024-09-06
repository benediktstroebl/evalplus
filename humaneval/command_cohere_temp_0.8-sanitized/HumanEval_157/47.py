def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle sides
    s = (a + b + c) / 2  # Hypotenuse
    p = (a**2 + b**2 - c**2) / (2 * b)  # Perpendicular
    h = (b**2 + c**2 - a**2) / (2 * c)  # Hypotenuse of the hypotenuse
    
    # Determine if it is a right-angled triangle
    return s * p == h ** 2