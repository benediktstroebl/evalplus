def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    if a == b == c:
        return True
    elif a == b + c or a + b == c or a == c + b:
        return True
    else:
        return False