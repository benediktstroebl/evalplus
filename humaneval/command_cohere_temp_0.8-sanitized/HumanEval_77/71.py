def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Check if the number is a perfect cube
    root = int(pow(a, (1/3)))
    return root ** 3 == a