
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if (x % 2)!= 0 or (y % 2)!= 0: #if x or y is not even, then -1
        return -1
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                return i
        return -1 #if all numbers are even
