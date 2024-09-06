def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    if a == 0 or b == 0 or c == 0:
        return False
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return True
    else:
        return False