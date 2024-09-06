
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n < 0:
        return 0
    if n < 10:
        return n
    if n % 2 != 0:
        return n // 2
    while True:
        n, remainder = divmod(n, 2)
        if remainder == 0:
            return n
