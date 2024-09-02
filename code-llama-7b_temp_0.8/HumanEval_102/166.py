
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    def _is_even(x):
        return True if x % 2 == 0 else False

    if (not isinstance(x, int) or not isinstance(y, int)
            or x <= 0 or y <= 0):
        raise ValueError("x and y should be positive integers")
    elif x > y:
        return -1
    else:
        # try to find an even number in the range [x, y]
        i = x
        while i <= y:
            if _is_even(i):
                return i
            i += 1
        return -1

