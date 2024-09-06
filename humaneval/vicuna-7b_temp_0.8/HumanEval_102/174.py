
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Add 1 to both x and y so that the range [x, y] is closed.
    # Otherwise, we might miss the smallest possible even number in the
    # range [x, y].
    x = (x + 1) // 2
    y = (y + 1) // 2

    # The function returns the biggest even integer in the range [x, y].
    while x < y:
        # Check whether the next integer is even and in the range [x, y].
        if x + 1 <= y and x + 1 % 2 == 0:
            return x + 1

        # Decrease x to the closest integer in the range [x, y].
        x += (y - x) // 2

    return -1
