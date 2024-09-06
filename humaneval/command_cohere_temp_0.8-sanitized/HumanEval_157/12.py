def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle
    s = (a**2 + b**2 + c**2) / 2
    aslope = a / s
    bslope = b / s
    cslope = c / s
    
    # Check for the presence of a right angle
    if aslope**2 + bslope**2 == c**2 or bslope**2 + cslope**2 == a**2 or cslope**2 + aslope**2 == b**2:
        return True
    else:
        return False