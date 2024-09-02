
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    n = str(n)

    if len(n) == 0:
        return 0
    for i in range(0, len(n)):
        if int(n[i]) % 2 != 0:
            product = product * int(n[i])
    return product

