
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # To implement, we should use only the multiplication and modulo operators for
    # the computations and use the walk-along-the-stairs algorithm for traversing the
    # tree.
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * n % 10
        n = n // 10
    return result

