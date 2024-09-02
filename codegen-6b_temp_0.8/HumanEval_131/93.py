
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return 1 if n % 2 else 0 if n % 10 == 0 else n // 10 * digits(n // 10)

