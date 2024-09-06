
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a while loop to compute the digits and make sure we don't overflow.
    # This is a bit of a hack, but it should work in practice.
    n_digits = 0
    while n > 0:
        n_digits = n % 10 + n_digits
        n = n / 10
    return n_digits
