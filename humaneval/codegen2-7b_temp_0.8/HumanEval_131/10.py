
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    i = 1
    while i < n:
        if i % 2:
            i *= i
        else:
            i += 1
    return i

