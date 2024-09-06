
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # we start from x because x is the first even integer and if
    # it's in the range, then it's the biggest.
    num = x
    while True:
        if num % 2 != 0:
            # num is odd
            num += 1
            continue
        if num >= x and num <= y:
            return num
        # num is bigger than y, so we return -1
        return -1

