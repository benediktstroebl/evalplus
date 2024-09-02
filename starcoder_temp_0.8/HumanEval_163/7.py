
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check if a and b are positive
    if (a < 0) or (b < 0):
        return None
    # check if a < b
    if a > b:
        return None
    # initial list to contain the even digits
    lst = []
    # loop over the numbers
    for n in range(a, b + 1):
        # get the even digits in the number
        if n % 2 == 0:
            lst.append(n)
    return lst
