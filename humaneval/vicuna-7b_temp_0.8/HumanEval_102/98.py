
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x <= y
    if x <= y:
        return y

    # Find the smallest integer number n such that x < n < y
    n = max(x, y)

    # Find the smallest integer k such that 2k is even and k is greater than n
    while True:
        k += 2
        if k >= n:
            break
        if k % 2 == 0:
            return n

    # If no such n exists, return -1
    return -1
