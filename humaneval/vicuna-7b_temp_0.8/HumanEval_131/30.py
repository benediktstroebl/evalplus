
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if n is a multiple of 10
    if n % 10 == 0:
        return 0
    # Check if n is odd
    if n % 10 == 1:
        return n
    # Check if n has only odd digits
    for i in range(1, len(str(n))):
        if str(n)[i] % 2 != 0:
            return 0
    return n
