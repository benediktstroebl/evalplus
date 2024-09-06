
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    return reduce(lambda x, y: int(x) * int(y), s[1::2]) if len(s) and s[-1] == '9' else reduce(lambda x, y: int(x) * int(y), s[1::2])


