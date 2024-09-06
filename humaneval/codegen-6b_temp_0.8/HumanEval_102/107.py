
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
    c = a
    d = b
    if a < b:
        a = b
        b = c
        c = d

    while c % 2 == 0:
        c /= 2

    while d % 2 == 0:
        d /= 2

    if b - a == c - d:
        return a
    else:
        return -1
