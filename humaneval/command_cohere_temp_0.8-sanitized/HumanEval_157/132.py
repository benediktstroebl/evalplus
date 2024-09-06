def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Check for Pythagorean triplets
    if hypotenuse == c and a == b + c:
        return True
    elif hypotenuse == c and b == c + a:
        return True
    elif hypotenuse == a and a == b + c:
        return True
    elif hypotenuse == b and b == c + a:
        return True

    # If none of the conditions are met, return False
    return False