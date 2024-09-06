
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    smaller = min(x,y)
    bigger = max(x,y)
    factors = []
    for i in range(1, smaller+1):
        if smaller % i == 0:
            factors.append(i)
        if len(factors) == 4:
            return -1
    return bigger if bigger % 2 == 0 else min(factors)
