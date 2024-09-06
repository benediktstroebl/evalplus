
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
    factorial = 1
    n_to_factorial = n
    while n_to_factorial > 0:
        factorial = factorial * n_to_factorial
        n_to_factorial -= 1
    return factorial

