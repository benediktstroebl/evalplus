
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
    n = as_int(n)
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    else:
        return pow(n, -1, 1) * (1 - pow(n, -1, 2)) * (1 - pow(n, -1, 3)) * ... * (1 - pow(n, -1, n-1))
