def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the cube root of the number
    root = int(pow(a, (1/3)))

    # If the cube root is an integer return True, else False
    return root == int(root)