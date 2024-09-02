
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # your code here
    if x > y:
        x, y = y, x
    if x % 2 == 0:
        return x
    else:
        while y >= x:
            if y % 2 == 0:
                return y
            else:
                y -= 1
        return -1
