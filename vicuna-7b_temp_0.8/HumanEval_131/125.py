
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # The loop is more readable with this helper function.
    # We use the fact that x % 2 == 1 if and only if x is odd.
    digits = [x % 2 for x in str(n)]
    if all(d for d in digits if d % 2 != 0):
        return 1
    return 0
