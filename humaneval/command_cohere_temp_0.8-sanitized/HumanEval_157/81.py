def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = sqrt(s*(s-a)*(s-b)*(s-c))  # Height

    # Determine if the triangle is right-angled using the Pythagorean theorem
    return h == b or h == a or h == c