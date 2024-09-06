
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if digit % 2 != 0:
            product *= digit
    return product

