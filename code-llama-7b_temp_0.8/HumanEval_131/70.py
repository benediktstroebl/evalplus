
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    total = 1
    if n < 0:
        raise ValueError('n must be a positive integer.')
    while n > 0:
        if n % 2 == 1:
            total *= (n % 10)
        n = n // 10
    return total

