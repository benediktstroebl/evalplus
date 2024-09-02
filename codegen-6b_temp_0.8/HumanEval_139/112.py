
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
    assert(n > 0), 'The input parameter n must be > 0'
    if n == 1:
        return 1
    elif n <= 4:
        return n * special_factorial(n - 1)
    else:
        return n * special_factorial(n - 1) * special_factorial(n - 2) * \
            special_factorial(n - 3) * special_factorial(n - 4)
