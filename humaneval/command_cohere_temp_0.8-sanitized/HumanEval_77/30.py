def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root n such that a = n * n * n
    n = int(pow(a ** (1/3)), 3)

    # Check if n * n * n equals a
    return n * n * n == a