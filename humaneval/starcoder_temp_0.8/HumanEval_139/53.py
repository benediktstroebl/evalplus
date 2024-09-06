
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
    if not isinstance(n, int) or n < 0:
        raise TypeError("Please supply a non-negative integer!")

    if n == 0:
        return 1

    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult
