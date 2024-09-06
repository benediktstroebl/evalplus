
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    if s[0] in ('0', '2', '3', '5'):
        return 0
    else:
        return n % 10 * (10 ** (len(s) - 1))
