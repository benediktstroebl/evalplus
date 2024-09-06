def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle
    s = (a ** 2 + b ** 2) ** 0.5
    t = (b ** 2 + c ** 2) ** 0.5
    # Check if the length of the third side is the hypotenuse of a right triangle
    return s == t or s**2 + c ** 2 == t ** 2  # Strict Equilateral or Cathetus (AAA or AA/S)