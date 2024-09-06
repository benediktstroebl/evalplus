def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root using integer division
    icbrt = int(a ** (1/3))

    # Check if the number is a cube of an integer
    return a == icbrt * icbrt * icbrt