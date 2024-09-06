
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    product = 1
    while n > 0:
        n, remainder = divmod(n, 10)
        product = product * remainder if remainder % 2!= 0 else product * remainder
    return product

