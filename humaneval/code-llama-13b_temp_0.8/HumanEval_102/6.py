
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # your code here
    if (x > y):
        return -1
    
    if (x % 2 == 0):
        if (y % 2 == 0):
            if (x <= y):
                return x
        else:
            if (y - 1 == x):
                return x
            else:
                return x + 2
    else:
        if (y % 2 == 0):
            if (y - 1 == x):
                return x
            else:
                return x + 1
        else:
            if (y - 1 == x):
                return -1
            else:
                return x + 2

