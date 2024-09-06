def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the greatest factor f of a which is a perfect cube and divides a exactly without a remainder
    for f in range(1, int(a ** (1/3)) + 1):
        if a % f == 0 and f ** 3 == a:
            return True

    return False