
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
    if not isinstance(n, int):
        raise TypeError(f"n must be an int; got {type(n)}")
    if n <= 0:
        raise ValueError(f"n must be > 0; got {n}")

    factorial = 1
    for i in range(n):
        factorial *= i + 1

    return factorial
