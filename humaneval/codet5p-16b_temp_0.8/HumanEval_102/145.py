
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if y < x:
        return -1
    else:
        num_list = []
        while x <= y:
            if x % 2 == 0:
                num_list.append(x)
            x += 1
        num_list = sorted(num_list)
        if len(num_list) == 0:
            return -1
        else:
            return num_list[-1]

