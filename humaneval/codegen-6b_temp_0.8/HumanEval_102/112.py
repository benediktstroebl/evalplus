
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    listx = range(x + 1)
    listy = range(y + 1)
    listx.reverse()
    listy.reverse()
    for i in listx:
        if i % 2 == 0:
            for j in listy:
                if i * j in range(x, y + 1):
                    return i * j
    return -1