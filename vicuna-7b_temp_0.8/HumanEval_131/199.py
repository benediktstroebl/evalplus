
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # The number is odd if it ends with a digit that is odd
    if (n % 10) % 2 == 1:
        # The product is 1, 2, 4, 6, 8, or 10
        # In this case, we add 2 to the product of the digits
        # In the worst case, the product of the digits is 10,
        # and we add 2 to get 12
        return 2 * (n // 10)
    else:
        # The number is even, and the product of the digits is 0
        return 0
