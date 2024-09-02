
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # your code here
    if x%2 == 0 and y%2 == 0:
        num_list = range(x,y+1)
        for n in num_list:
            if n%2 == 0:
                return n
    return -1
