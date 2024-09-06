def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    if (a == 0 or b == 0 or c == 0) and (a + b > c) and (a + c > b) and (b + c > a):
        return True
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return True
    return False