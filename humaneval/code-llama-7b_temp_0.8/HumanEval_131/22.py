
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    for d in str(n):
        d_int = int(d)
        if d_int % 2:
            prod *= d_int
    return prod


