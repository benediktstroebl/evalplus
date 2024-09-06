
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    a = (x + y) // 2
    b = x + y - a * 2
    while b > a * 2:
        a = (a + b) // 2
        b = x + y - a * 2
    return a
