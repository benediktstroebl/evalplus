def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root using integer division
    cube_root = a ** (1/3)

    # Check if the cube root is an integer
    if not cube_root.is_integer():
        return False

    # If all conditions are met, return True
    return True