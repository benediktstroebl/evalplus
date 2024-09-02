
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    a = str(n)
    b = 0
    for i in a:
        if i%2 != 0:
            b *= int(i)
    return b if b != 0 else 0
