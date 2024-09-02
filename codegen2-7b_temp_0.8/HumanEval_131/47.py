
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
    for d in range(2, n+1, 2):
        if n % d == 0:
            return d * digits(n // d)
    return
