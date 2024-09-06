def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root of the number
    cube_root = int(pow(a, 1/3))

    # Check if the cube root is an integer and the equality holds
    return cube_root ** 3 == a