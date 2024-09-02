
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
    for i in n:
        if int(i)%2 == 0:
            product = 0
            break
        else:
            product = product * int(i)
    return product
