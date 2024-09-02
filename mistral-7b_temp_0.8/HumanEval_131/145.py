
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # d = n % 10
    # if d%2 == 0:
    #     return 0
    # n = n // 10
    # return n * d

    if not n:
        return 0

    res = 1
    while n:
        d = n % 10
        if d % 2 == 1:
            res = res * d
        n //= 10
    return res
