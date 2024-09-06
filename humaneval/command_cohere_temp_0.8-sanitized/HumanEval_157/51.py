def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle with the greatest angle
    s = (a + b + c) / 2
    t = (math.sqrt(s * (s - a) * (s - b) * (s - c))).chio()
    
    return t == 1 or t == 0 or t ==-1