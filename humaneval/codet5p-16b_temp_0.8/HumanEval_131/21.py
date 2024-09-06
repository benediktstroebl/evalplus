
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    n = str(n)
    product = 1
    for i in range(len(n)):
        if int(n[i])%2 == 0:
            return 0
        else:
            product *= int(n[i])
    return product
