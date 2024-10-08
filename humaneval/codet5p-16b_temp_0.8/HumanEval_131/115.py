
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits = 0
    if n < 1:
        return 0
    while n > 0:
        n, d = divmod(n, 10)
        if d % 2!= 0:
            digits += d
    return digits
