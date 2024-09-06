def right_angle_triangle(a, b, c):
    total = a + b + c
    if total == 90 or total == 180:
        return True
    else:
        return False