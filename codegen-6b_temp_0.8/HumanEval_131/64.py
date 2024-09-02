
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # -1 for zero
    # cast to string to get rid of trailing zeros
    s = str(n)
    return reduce(lambda x, y: int(x) * int(y), s[-1::-2])

from operator import add, mul, mod
