
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    n = abs(n)
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            prod *= d
        n = n // 10
    return prod
