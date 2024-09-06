
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    even_lst = []
    for i in range(x, y + 1):
        if i % 2 == 0:
            even_lst.append(i)
    if len(even_lst) == 0:
        return -1
    return max(even_lst)
