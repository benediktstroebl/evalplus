
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 10:
        return n

    str_n = str(n)
    prod = 1

    for c in str_n:
        if int(c) % 2 == 1:
            prod *= int(c)

    return prod

