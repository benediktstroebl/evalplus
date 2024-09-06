
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # binary digits
    d = 0
    # check for even numbers
    while n:
        d *= 10
        n //= 10
    return d
