
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = str(n)
    result = 1
    for c in n:
        if int(c) % 2 != 0:
            result *= int(c)
    return result

