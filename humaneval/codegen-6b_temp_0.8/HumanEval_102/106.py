
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    if x % 2 == 0 and y % 2 == 0:
        n = min(x, y) // 2
        while n > 0 and n % 2 == 0:
            n //= 2
        return n
    elif x % 2 == 0:
        return x // 2
    elif y % 2 == 0:
        return y // 2
    else:
        return -1
    