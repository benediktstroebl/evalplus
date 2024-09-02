
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n % 2 == 0:
        return 0
    d = n
    s = 0
    while d > 0:
        s += d % 10
        d = int(d / 10)
    return s
