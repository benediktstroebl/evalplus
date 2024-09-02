
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits = []
    product = 1
    for i in str(n):
        if i % 2:
            digits.append(int(i))
    if len(digits) > 0:
        product = 1
        for i in digits:
            product = product * i
    else:
        product = 0
    return product
