
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # if x or y is not a number or not positive, return -1
    if type(x) != int or x <= 0 or type(y) != int or y <= 0:
        return -1
    # if x is greater than y, return -1
    if x > y:
        return -1
    # if x is even, return x
    if x % 2 == 0:
        return x
    # if y is even, return y
    if y % 2 == 0:
        return y
    # if none of the conditions are true, return -1
    return -1
