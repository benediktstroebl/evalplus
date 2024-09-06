
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even, return 0 if so
    for i in range(n):
        if n % i == 0:
            return 0
    # Otherwise, the last digit must be odd
    return n % (n // 10) + 1
