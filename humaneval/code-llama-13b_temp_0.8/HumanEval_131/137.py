
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    m = 1
    for d in str(n):
        d = int(d)
        if d % 2 == 1:
            m *= d
    return m

