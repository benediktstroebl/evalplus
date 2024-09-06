def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  #semi-perimeter of the triangle
    # Check if the triangle is right-angled
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else: 
        return False