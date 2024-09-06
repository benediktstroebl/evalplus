
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0: return 0
    if n == 1: return 1
    if n % 2 == 0: return 0

    digits = 1
    while n > 1:
        if n % 2:
            digits *= n % 10
            n = n // 10
        else:
            n //= 10
    return digits
