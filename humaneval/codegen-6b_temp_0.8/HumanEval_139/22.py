
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
    n_factorial = 1

    if n > 1:
        n_factorial = n_factorial * n

        for i in range(1, n):
            n_factorial = n_factorial * (n - i)

    return n_factorial

