
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # The function works by iteratively trying smaller and smaller values
    # for the number to be returned until we find one that meets the
    # requirements.

    # Note that the function also has a return -1 case.

    # We first try the number x. If it's even and in the range [x, y],
    # we're done.
    if x % 2 == 0 and x <= y:
        return x

    # If x is not even or is outside the range [x, y], we try the number
    # y. If it's even and in the range [x, y], we're done.
    if y % 2 == 0 and y <= x:
        return y

    # If neither x nor y is even or is outside the range [x, y], we
    # have to check all the numbers in the range [x, y].
    # Note that there are two numbers in the range [x, y] that we
    # don't have to check: x and y themselves.
    # We use a for loop to iterate over the remaining numbers
    for i in range(x, y+1):
        if i % 2 == 0:
            return i

    # If we get here, we haven't found an even number in the range [x, y].
    # This is the case we handle with the return -1 statement.
    return -1
