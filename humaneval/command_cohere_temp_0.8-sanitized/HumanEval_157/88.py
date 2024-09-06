def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == 0 or b == 0 or c == 0) and (a + b == c or a + c == b or b + c == a):
        return True
    else: 
        numer = (a**2 + b**2 + c**2) / 2 - sqrt((b**2 + c**2 - a**2) / 2) ** 2
        denom = (a**2 + b**2 + c**2) / 2 + (b**2 + c**2 - a**2) / 2 
        return numer == denom