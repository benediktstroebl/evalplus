
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    a = x
    b = y
    while a < b:
        x = random.randrange(a, b + 1)
        y = random.randrange(a, b + 1)
        if x % 2 == 0 and y % 2 == 0:
            return x, y
        a += 1
        b += 1
    return -1, -
