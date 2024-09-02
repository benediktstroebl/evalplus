
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

    # Brazilian factorial is undefined for non-positive integers
    if n <= 0:
        raise ValueError("The input must be a positive integer.")

    total = 1
    for i in range(n, 1, -1):
        total *= i
    return total
