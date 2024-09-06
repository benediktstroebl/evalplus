def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the integer cube root of the number
    cube_root = int(pow(a, (1/3)))

    # Check if the original number is equal to the cube
    return a == cube_root ** 3