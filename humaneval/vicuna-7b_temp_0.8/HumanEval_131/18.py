
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    while n > 0:
        n, r = divmod(n, 2)
        if r % 2 != 0:
            return r
    return 0
