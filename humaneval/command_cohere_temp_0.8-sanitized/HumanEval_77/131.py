def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the smallest factor of a which is also a cube
    for i in range(1, int(a**(1/3)) + 1):
        if a % i == 0 and iscube(i):
            return True
    return False