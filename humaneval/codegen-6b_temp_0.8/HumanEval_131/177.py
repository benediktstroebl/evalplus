
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    l = len(str(n))
    if l % 2 == 0:
        return 0
    else:
        return int(str(n)[:(l-1)]) * int(str(n)[l-1])

