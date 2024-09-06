
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Check the input
    if not isinstance(x, int):
        raise TypeError("Expected type is int, got {}".format(type(x)))
    if not isinstance(y, int):
        raise TypeError("Expected type is int, got {}".format(type(y)))
    if x < 0:
        raise ValueError("Expected positive int value, got {}".format(x))
    if y < 0:
        raise ValueError("Expected positive int value, got {}".format(y))
    if x > y:
        raise ValueError("x should be less than y, got {} and {}".format(x, y))
    
    if y % 2 == 1:
        return -1
    else:
        return max(z for z in range(x, y+1) if z % 2 == 0)


