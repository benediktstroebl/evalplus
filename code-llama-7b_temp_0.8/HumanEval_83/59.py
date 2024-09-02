
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # let's do it with binary search
    import math
    # it is enough to count all numbers with more significant digits
    # let's shift the value by one
    n += 1
    # let's put it as a binary number
    n_bin = bin(n)[3:]
    # count all ones
    n_ones = n_bin.count('1')
    # and calculate the count
    return 2 ** (n_ones - 1) * math.comb(n_ones, 2)

