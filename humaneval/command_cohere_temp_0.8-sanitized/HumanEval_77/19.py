def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the largest cube root that is less than or equal to a
    for i in range(1, int(a ** (1/3)) + 1):
        if i * i * i == a:
            return True

    return False