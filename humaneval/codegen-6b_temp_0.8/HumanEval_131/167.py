
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    for i, x in enumerate(str(n)[::-1]):
        if int(x) % 2 != 0:
            return i
    return 0

