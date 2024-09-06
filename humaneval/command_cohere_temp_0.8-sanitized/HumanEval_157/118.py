def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + a ** 2 == c ** 2:
        return True
    else:
        return False