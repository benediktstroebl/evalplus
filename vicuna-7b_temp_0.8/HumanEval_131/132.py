
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    if (n % 2) == 0:
        return 0
    # If the number of odd digits is 0, return 0
    if len(str(n)[::2]) == 0:
        return 0
    # Calculate the product of the odd digits
    return n // (2**len(str(n)[::2]))
