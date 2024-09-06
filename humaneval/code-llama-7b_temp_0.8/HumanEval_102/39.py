
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    max_num = max(x, y)
    min_num = min(x, y)

    # Check for even number
    if max_num % 2 == 0 and max_num > min_num:
        return max_num
    elif min_num % 2 == 0 and max_num > min_num:
        return min_num

    # Check for odd number
    if max_num % 2 == 1 and max_num > min_num + 1:
        return max_num - 1
    elif min_num % 2 == 1 and max_num > min_num + 1:
        return min_num + 1

    # No even or odd number within range
    return -1

