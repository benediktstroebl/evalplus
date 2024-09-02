
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
    return pow(n, n) * pow(n-1, n-1) * pow(n-2, n-2) * \
        pow(n-3, n-3) * ... * pow(2, 0) * pow(1, 1)
