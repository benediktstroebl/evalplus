def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    leg1 = ((b**2) + (c**2) - (a**2))**0.5
    leg2 = ((a**2) + (c**2) - (b**2))**0.5
    
    # Check if the length of the two legs form a right angle
    if leg1**2 + leg2**2 == a**2:
        return True
    else:
        return False