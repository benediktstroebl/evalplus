
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = str(n)
    s = 0
    for x in num:
        if int(x) % 2 != 0:
            s *= int(x)
    return s
