
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    import math

    # n is a positive integer, so it can be represented as a power of 10
    # with an integer coefficient
    m = int(math.log10(n))
    # if n is odd, the product of the odd digits is n
    if m % 2 == 0:
        return 0
    else:
        return n

    return 0

