
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x == y:
        return x
    elif x > y:
        return -1
    else:
        mid = (x + y) // 2
        if mid % 2 == 0:
            return mid
        elif (x + mid) // 2 % 2 == 1:
            return mid + 1
        else:
            return mid - 1

