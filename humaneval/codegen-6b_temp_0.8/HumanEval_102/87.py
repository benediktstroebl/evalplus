
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        raise ValueError('x should be <= y')

    if x % 2 != 0 or y % 2 != 0:
        return - 1

    if x <= 3:
        return x

    if x > 19 and x <= 31:
        return int((x - 4) * x // 2 + 10)

    if x > 31 and x <= 63:
        return int((x - 4) * x // 2 + 20)

    if x > 63 and x <= 127:
        return int((x - 4) * x // 2 + 30)

    if x > 127 and x <= 255:
        return int((x - 4) * x // 2 + 40)

    if x > 255:
        return -1

