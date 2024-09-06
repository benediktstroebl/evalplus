
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    def is_even(n):
        if n % 2 == 0:
            return True
        return False
    if is_even(x) and is_even(y):
        if x > y:
            return y
        elif x == y:
            return y
        else:
            return x
    else:
        if x % 2 != 0 or y % 2 != 0:
            if x > y:
                return x
            elif x == y:
                return x
            else:
                return y
        else:
            if x > y:
                return y
            elif x == y:
                return y
            else:
                return -1


