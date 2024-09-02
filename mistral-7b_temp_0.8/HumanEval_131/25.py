
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here

    product = 1
    if n < 1:
        return 0
    n = str(n)
    for d in n:
        if int(d) % 2 != 0:
            product *= int(d)
    return product

