def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root of the number
    cube_root = int(pow(a, (1/3)))

    # Check if the cube root is an integer and the input is the cube of that integer
    return cube_root == int(cube_root) and a == cube_root ** 3