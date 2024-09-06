def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total * total == Pythagorean_Theorem(a, b, c)
def Pythagorean_Theorem(a, b, c):
    return (a**2 + b**2) == c**2