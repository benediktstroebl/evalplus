
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Read the digits of n as a list
    digits = [int(d) for d in str(n)]
    # Check if all digits are even
    if all(d % 2 == 0 for d in digits):
        return 0
    # Compute the product of all odd digits
    product = 1
    for digit in digits:
        if digit % 2 != 0:
            product *= digit
    return product
