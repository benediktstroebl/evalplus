
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # check if the range of x and y is from 1 to n
    if x > y:
        return -1

    if x > y and x % 2 == 0:
        return x

    if y > x and y % 2 == 0:
        return y

    if x > y and x % 2 == 0:
        return max(x, y)

    return -1
