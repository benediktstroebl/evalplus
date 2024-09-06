
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    if n < 10:
        return n
    while n != 0:
        if n % 10 % 2 == 1:
            prod = prod * (n % 10)
        n = n // 10
    if prod == 1:
        return 0
    return prod
