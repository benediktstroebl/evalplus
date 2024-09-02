
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Our base case is when y <= x
    if y <= x:
        return -1

    # Our recursive case is that we're not at a base case, and y is even, 
    # and x <= y
    elif (y % 2) == 0:
        if x <= y:
            return y
        else:
            return choose_num(x, y-2)

    # Finally, if none of the above are true, then y is odd, so we want to 
    # reduce by 1, and check again
    else:
        return choose_num(x, y-1)
