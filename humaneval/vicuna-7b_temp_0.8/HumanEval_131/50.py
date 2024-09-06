
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # recursive call with divisor - n
    # and divisor - n + 1
    return 0 if n % 2 == 0 else (n // 2) * (n // 2) + (n // 2)
