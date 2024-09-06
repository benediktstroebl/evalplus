def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == 0 or b == 0 or c == 0) or (a == b or b == c or a == c):
        return False
    else:
        s = (a**2 + b**2 + c**2) / 2
        return s**0.5 == abs(a) or s**0.5 == abs(b) or s**0.5 == abs(c)