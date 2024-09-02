
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not (type(n) == int and n > 0):
        return None
    n = str(n)
    # print(n)
    # n = n[::-1]
    # print(n)
    product = 1
    for c in n:
        c = int(c)
        # print(c)
        if c % 2 == 0:
            continue
        else:
            product *= c
    if product == 1:
        return 0
    return product
