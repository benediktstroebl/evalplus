
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    products = 1
    for i in range(len(str(n))):
        digits = int(str(n)[i])
        if digits % 2 != 0:
            products *= digits
    return products

