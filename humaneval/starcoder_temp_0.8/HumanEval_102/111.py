
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # The base case.
    if x >= y:
        return -1

    # Find the midpoint of the range.
    mid = (x + y) // 2

    # If the midpoint is even, check whether it's the answer.
    if mid % 2 == 0:
        if (mid >= x) and (mid <= y):
            return mid
        # If it's not the answer, check the rest of the range.
        return choose_num(x, mid - 1)

    # If the midpoint is odd, check whether it's the answer.
    elif (mid + 1 >= x) and (mid + 1 <= y):
        return mid + 1
    # If it's not the answer, check the rest of the range.
    return choose_num(mid + 2, y)
