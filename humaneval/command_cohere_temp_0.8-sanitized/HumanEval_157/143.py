def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle
    s = (a ** 2 + b ** 2 + c ** 2) / 2
    as_ = sqrt(max(0, s - c ** 2))
    bs_ = sqrt(max(0, s - a ** 2))
    cs_ = sqrt(max(0, s - b ** 2))
    
    # Check if the length of the sides satisfy the conditions of a right angled triangle
    if as_ + bs_ == c and as_ + cs_ == b and bs_ + cs_ == a:
        return True
    else:
        return False