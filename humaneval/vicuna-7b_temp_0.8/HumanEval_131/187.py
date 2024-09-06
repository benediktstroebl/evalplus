
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Get the digits of n as a list of integers
    digits = [int(d) for d in str(n)]
    # If all digits are even, return 0
    if all(d % 2 == 0 for d in digits):
        return 0
    # Otherwise, compute the product of the odd digits
    product = 1
    for d in digits:
        if d % 2 == 1:
            product *= d
    return product
