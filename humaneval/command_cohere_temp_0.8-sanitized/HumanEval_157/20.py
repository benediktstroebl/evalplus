def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total == sq(a) + sq(b)
def sq(a):
    return a * a