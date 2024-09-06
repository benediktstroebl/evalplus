
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    #return 
    # choose_num(x, y) = min{evenNumber in [x, y]}
    # even number = even(x) if x is even
    #             = even(y) if y is even
    #             = even(x + 1) otherwise
    
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        return choose_num(y, x)
    if y - x == 0:
        if y % 2 == 0:
            return y
        else:
            return y - 1
    if x % 2 == 0:
        if x + 2 <= y:
            return x + 2
        else:
            return x
    if x % 2 == 1:
        if x + 1 <= y:
            return x + 1
        else:
            return x
    
