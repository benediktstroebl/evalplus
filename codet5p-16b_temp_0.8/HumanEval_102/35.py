
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x < y:
        if x % 2 == 0 and y % 2 == 0:
            x_new = y
            y_new = x
            if x < y:
                for num in range(x_new, y_new + 1):
                    if num % 2 == 0:
                        return num
                return -1
            return -1
        return -1
    return -1

