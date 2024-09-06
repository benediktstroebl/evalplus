def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the greatest factor f of a which is also a cube
    for i in range(2, int(a**(1/3)) + 1):
        if a % i == 0:
            f = i
            while a % f == 0:
                a //= f
            if a == 1:
                return True

    return False