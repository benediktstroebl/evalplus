def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root using integer division
    cube_root = a ** (1/3)

    # Check if the number is a perfect cube
    return a == cube_root ** 3