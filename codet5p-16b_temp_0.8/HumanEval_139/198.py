
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

    factorial_1 = 1
    factorial_2 = 1
    for num in range(1, n+1):
        factorial_1 *= num
    for num in range(1, n-1):
        factorial_2 *= num
    return factorial_1 * factorial_2
