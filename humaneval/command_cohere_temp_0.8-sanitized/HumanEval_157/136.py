def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return True
    else:
        return False