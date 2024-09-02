
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Find the smallest number greater than both x and y
    m = min(x, y)

    # Check if m is even and if it's the smallest even number in the range
    if m % 2 == 0 and m > max(x, y):
        return m

    # If there's no smallest even number, return -1
    else:
        return -1
