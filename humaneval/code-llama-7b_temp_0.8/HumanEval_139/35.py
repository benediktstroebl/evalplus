
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

    if n < 0:
        raise ValueError(
            'The value must be greater than or equal to 0.')

    special_factorial = 1

    while n > 0:
        special_factorial *= n
        n -= 1

    return special_factorial
