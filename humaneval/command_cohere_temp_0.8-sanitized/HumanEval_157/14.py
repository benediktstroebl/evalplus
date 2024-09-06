def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine the difference between the two other sides and the hypotenuse
    if abs(a - b) > s / 2 or abs(b - c) > s / 2 or abs(c - a) > s / 2:
        return True
    else:
        return False