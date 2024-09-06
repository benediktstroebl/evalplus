
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x<=y:
        n = 0
        if x%2 == 0 and x<=y:
            while n*2 < y:
                n = n+2
            return n
        elif x%2 == 0 and y<=x:
            while n*2 < x:
                n = n+2
            return n
        elif x%2 != 0 and x<=y:
            while n < y:
                n = n+2
            return n
        else:
            return -1
    else:
        return -1


assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(13, 2) == -1
assert choose_num(0, 0) == -1
assert choose_num(16, 17) == -1
