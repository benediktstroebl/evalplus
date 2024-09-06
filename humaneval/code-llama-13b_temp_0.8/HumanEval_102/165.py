
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # The function returns -1 if there's no such number.
    result = -1
    # We loop through the numbers from x to y.
    for i in range(x, y + 1):
        # And check if they are even.
        if i % 2 == 0:
            # If they are, we store them in the variable result and break.
            result = i
            break
    # Finally, we return the result.
    return result

