
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # The special factorial of 0 is 1, because there is only 1 way to arrange 0
    # things.
    if n == 0:
        return 1
    else:
        # The special factorial is calculated by multiplying n! by (n-1)!
        # and summing these products from 1 to n.
        return (n * (n-1)) / 2 * special_factorial(n-1)
