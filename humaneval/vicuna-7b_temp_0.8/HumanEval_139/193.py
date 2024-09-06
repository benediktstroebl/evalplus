
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
    # pylint: disable=too-many-return-statements
    # pylint: disable=too-many-branches
    n = as_int(n)
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return n * special_factorial(n-1)
    # pylint: enable=too-many-return-statements
    # pylint: enable=too-many-branches
