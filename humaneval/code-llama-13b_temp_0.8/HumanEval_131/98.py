
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    p = 1
    for d in str(n):
        if int(d)%2 == 0:
            pass
        else:
            p *= int(d)
    return p
