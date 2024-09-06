
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if all(d % 2 != 0 for d in n // 10):
        return n // 10 * 10
    else:
        return 0
