
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # if all digits are even, return 0
    if all(c % 2 == 0 for c in str(n)):
        return 0

    # otherwise, compute the product of the odd digits and return it
    product = 1
    for digit in str(n)[1:]:
        if digit % 2 != 0:
            product *= digit
    return product
