
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    elif n < 0:
        n = -1*n
    if n % 2 == 0:
        return 0
    else:
        p = 1
        while n >= 10:
            r = n % 10
            p = p * r
            n = n // 10
            r = n % 10
        p = p * n
    return p
