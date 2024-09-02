
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    assert n > 0
    n2 = n
    n = n // 2
    while n > 0:
        if n % 10 == odd(n2):
            return n
        n = n // 10
    return 0

