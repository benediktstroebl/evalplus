
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
    # No need to check if n is positive, as the function is only defined for
    # positive integers.
    # Also, the code is more readable if it doesn't raise an exception.
    return n * special_factorial(n-1) * special_factorial(n-2) * ... * special_factorial(1)
