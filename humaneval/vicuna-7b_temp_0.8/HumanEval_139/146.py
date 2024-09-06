
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
    # Take the factorial of all the positive integers less than or equal to n
    # Multiply them together and subtract 1
    return pow(n, n-1) * pow(n-1, n-2) * ... * pow(2, n-1) * (1-1)
