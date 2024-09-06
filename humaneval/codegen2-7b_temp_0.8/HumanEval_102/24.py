
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if (x <= y):
        a = x
        b = y
    else:
        a = y
        b = x
    while a % 2!= 0:
        a = a + 1
    while b % 2!= 0:
        b = b - 1
    if a <= b:
        return a
    else:
        return b
    
