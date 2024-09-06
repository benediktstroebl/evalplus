
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # convert to float to avoid integer division
    x = float(x)
    y = float(y)
    if x > y:
        return -1
    z = (x + y) / 2
    if z % 1 == 0:
        return int(z)
    else:
        z = int(z) + 1
        if z <= y:
            return z
        else:
            return -1

    # Test your code
    print choose_num(12, 15)
    print choose_num(13, 12)
