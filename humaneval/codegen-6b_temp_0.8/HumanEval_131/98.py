
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # We could probably do better with high-order Python functions (Python's
    # built-in modulo operator, or some equivalent), but this is a
    # little-or-no solution.
    product = 1
    while n:
        product *= (n % 10)
        n //= 10
    return product
