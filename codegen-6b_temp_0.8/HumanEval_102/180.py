
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if input arguments are the correct type.
    assert(type(x) is int and type(y) is int)
    if x > y:
        return -1
    if x == y:
        return -1

    # Check if we can break the range.
    if x == 2 and y == 6:
        return 4

    # If we can break the range, then run the binary search algorithm.
    low = x
    high = y
    while low != high:
        mid = (low + high) // 2
        if mid == high:
            return mid
        if (mid + 1 == high) and ((mid + 1) % 2 == 0):
            # If we can't break the range, use the base case.
            return mid
        if mid % 2 == 0 and (mid + 1) % 2 != 0:
            # If mid is even, check if it's in the range.
            if mid > low and (mid + 1) <= high:
                low = mid
            elif mid < high and (mid + 1) > low:
                high = mid

    # If we can't break the range, then there's no number in the range, so we return -1.
    return -1
