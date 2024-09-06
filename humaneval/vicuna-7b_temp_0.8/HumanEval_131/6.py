
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # A brute-force solution is to iterate over the digits of n,
    # and for each digit, check if it is odd and multiply it by the
    # remaining digits. If a digit is even, multiply by the power of 2
    # corresponding to its position.
    #
    # However, this solution is not very efficient, as the number of
    # digits of n grows with n.
    #
    # Instead, we can use the fact that the sum of the digits of n is
    # the same as the sum of the digits of its reciprocal (1/n).
    #
    # This allows us to efficiently calculate the product of the odd
    # digits by computing the reciprocal of n, and then taking the
    # product of the odd digits of the reciprocal.
    n = int(n)
    if n < 0:
        raise ValueError("n must be a positive integer.")
    if n == 0:
        return 0
    if not n % 2:
        return 1
    return (1 << (len(str(n)) - 1)) * (n // 2)
