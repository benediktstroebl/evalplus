
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
    if n < 1:
        return 1

    if n == 1:
        return 1

    # Using the formula, calculate the special factorial
    result = n
    for i in range(2, n):
        result *= i

    return result