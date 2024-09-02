
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    def is_even(n):
        return n % 2 == 0

    def is_bigger(a, b):
        return a > b
    
    if not is_even(x) and not is_even(y):
        return -1
    elif is_even(x) and not is_even(y):
        if is_bigger(x, y):
            return x
        else:
            return y
    elif not is_even(x) and is_even(y):
        if is_bigger(x, y):
            return y
        else:
            return x
    elif is_even(x) and is_even(y):
        if is_bigger(x, y):
            return y
        else:
            return x
