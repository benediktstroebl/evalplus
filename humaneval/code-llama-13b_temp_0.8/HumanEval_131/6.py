
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    if n < 0:
        return product
    for i in str(n):
        if int(i) % 2 == 0:
            continue
        else:
            product *= int(i)
    return product

