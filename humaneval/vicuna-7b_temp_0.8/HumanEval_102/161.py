
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x or y are even
    if x % 2 == 0 or y % 2 == 0:
        return max(x, y)
    # If not, check if there's a number in the range that is even and bigger
    # than both x and y
    odd_number = min(x, y)
    for i in range(x, y + 1):
        if (i % 2) == 0:
            return i
    return -1
