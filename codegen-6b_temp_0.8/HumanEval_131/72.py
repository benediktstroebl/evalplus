
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    else:
        return n % 10 * digits(n // 10)

"""
Parameters

n: a positive integer, the number of steps to take on the staircase
Returns

The number of ways to reach the top, n steps
"""