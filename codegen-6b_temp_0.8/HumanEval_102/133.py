
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    result = -1
    low = max(x, y)
    high = min(x, y)
    for i in range(low, high+1):
        if i % 2 == 0:
            result = i
    return result








