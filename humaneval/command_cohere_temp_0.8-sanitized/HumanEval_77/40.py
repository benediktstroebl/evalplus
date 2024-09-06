def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the greatest factor f of a which is also a perfect cube
    f = a ** (1/3)
    while not f ** 3 == a:
        f = f + 1

    # If f is the greatest factor of a, then a is a cube
    return f ** 3 == a