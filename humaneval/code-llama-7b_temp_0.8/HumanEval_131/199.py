
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # it's more elegant to use the bitwise operator:
    # n & 1 == 1
    # if n is odd
    # n >> 1 == n / 2
    # if n is even
    # n >> 1 == n / 2 and rounded
    return sum(digit*(n & 1) for n, digit in enumerate(map(int, str(n)), 1) if n & 1)
