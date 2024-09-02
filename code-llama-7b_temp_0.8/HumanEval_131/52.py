
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 0
    elif n % 2 == 1:
        return reduce(lambda x, y: x*y, [d for d in str(n) if int(d) % 2 == 1], 1)
    return n
