
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Your code goes here
    if x < y and y % 2 == 0:
        return y
    elif x < y and y % 2 == 1:
        return choose_num(x, y - 1)
    elif x >= y and y % 2 == 0:
        return -1
    elif x >= y and y % 2 == 1:
        return choose_num(x - 1, y)
