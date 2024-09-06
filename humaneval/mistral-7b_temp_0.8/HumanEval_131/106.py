
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    i = 0
    if len(str(n)) == 1:
        return 0
    while i < len(str(n)):
        if (i + 1) % 2 == 0:
            i += 1
        else:
            product *= int(str(n)[i])
            i += 1
    return product
