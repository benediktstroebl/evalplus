
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    n = (y - x) // 2
    for i in range(n, -1, -1):
        if x + i * 2 > y:
            continue
        if x + i * 2 == y:
            return x + i * 2
        elif x + i * 2 < y:
            continue

    return -1

