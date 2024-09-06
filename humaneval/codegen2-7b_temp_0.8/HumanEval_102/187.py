
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    num_range = range(x, y+1)
    for i in num_range:
        if is_even(i) and is_even(i+1):
            return i
    return -1

