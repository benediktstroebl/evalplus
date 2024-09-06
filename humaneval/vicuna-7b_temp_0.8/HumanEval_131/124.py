
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for 0 or 1 in the front
    if n < 2 or n % 2 != 0:
        return 0
    # Check for all digits being even
    for i in range(1, n // 2):
        if n % i != 0:
            return 0
    # Check for odd digits in the front
    if n % 2 != 0:
        return n // 2
