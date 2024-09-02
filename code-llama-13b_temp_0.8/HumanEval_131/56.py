
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    last = 1
    while n >= 10:
        last *= n % 10
        n = int(n / 10)
    return n * last

