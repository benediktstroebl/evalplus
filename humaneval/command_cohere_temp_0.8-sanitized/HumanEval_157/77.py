def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else: 
        return False