
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x is greater than y
    if x > y:
        # If y is even, the maximum number is y
        if y % 2 == 0:
            return y
        # If y is odd, the maximum number is the next even integer after y
        else:
            return y + 1
    # If y is greater than x, the result is the same as the above case
    else:
        # Check if y is even
        if y % 2 == 0:
            return y
        # If y is odd, the maximum number is the next even integer after x
        else:
            return x + 1