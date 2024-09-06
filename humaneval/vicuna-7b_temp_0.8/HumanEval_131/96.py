
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # p = 1
    # d = 10
    # while p <= n:
    #     d //= 10
    #     p *= 10
    # return p
    while n > 0:
        n //= 11
        p *= 11
    return p
