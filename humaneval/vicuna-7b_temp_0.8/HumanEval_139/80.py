
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
    # The formula is n! * (n-1)! * (n-2)! * ... * 1!
    # To calculate the special factorial, multiply the factorial of n and
    # subtract 1, then multiply the result by the factorial of n-1 and subtract
    # 2, and so on.
    return n * (n-1) * (n-2) * ... * 1
