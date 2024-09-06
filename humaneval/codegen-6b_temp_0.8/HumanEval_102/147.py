
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # if numbers are consecutive
    if x == y:
        return -1 

    if x % 2 == 0:
        # if number is even
        if x <= y:
            middle = (x + y) // 2
        elif y % 2 == 0:
            middle = (x + y + 1) // 2
        else:
            middle = (x + y - 1) // 2
        
        return middle

    if x % 2 != 0:
        # if number is odd
        if x <= y:
            middle = (x + y) // 2 + 1
        elif y % 2 == 0:
            middle = (x + y + 1) // 2 + 1
        else:
            middle = (x + y - 1) // 2 + 1

        return middle

