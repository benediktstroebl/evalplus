
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    assert x > 0 and y > 0 and type(x) == int and type(y) == int, 'Invalid input'
    if y % 2 == 1:
        y -= 1

    if x % 2 == 0:
        if x < y:
            return y
        return x
    elif x < y:
        return x + 2
    return x

