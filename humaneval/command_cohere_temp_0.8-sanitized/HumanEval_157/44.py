def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle with the greatest angle
    s = (a + b + c) / 2  # the semi-perimeter of the triangle
    r = sqrt(s * (s - a) * (s - b) * (s - c))  # the radius of the circle inscripted the triangle

    return r == abs(a - b) or r == abs(a - c) or r == abs(b - c)