def right_angle_triangle(a, b, c):
    total = a + b + c
    if total * total == a * a + b * b + c * c:
        return True
    else: 
        return False