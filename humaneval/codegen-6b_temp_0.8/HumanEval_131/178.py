
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    ix = 0
    for c in s:
        if int(c) % 2 == 1: return int(c)
        ix += 1
    return 0
