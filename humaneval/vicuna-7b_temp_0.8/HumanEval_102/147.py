
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check for the case where y is greater than x
    if y > x:
        return max(x, (x + y) // 2)

    # Check for the case where x is greater than y
    if x > y:
        return max(y, (x + y) // 2)

    # Check for the case where x is equal to y
    if x == y:
        return max(x, y)

    # No such even integer number in the range
    return -1
