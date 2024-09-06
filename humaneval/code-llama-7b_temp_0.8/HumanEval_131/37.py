
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    prod = 1
    for d in s:
        if int(d) % 2 == 1:
            prod *= int(d)
    return prod

