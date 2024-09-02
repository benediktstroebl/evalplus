
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    elif x == y:
        return x
    elif x%2 == 0 and y%2 == 0:
        if y < x+2:
            return y
        else:
            return choose_num(x, y-2)
    elif x%2!= 0 and y%2!= 0:
        if y < x+1:
            return y
        else:
            return choose_num(x, y-1)
    elif x%2!= 0 and y%2 == 0:
        return -1
    elif x%2 == 0 and y%2!= 0:
        return x
