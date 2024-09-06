def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == b + c) or (a == c + b) or (b == c + a) or (c == a + b):
        return True
    else:
        return False