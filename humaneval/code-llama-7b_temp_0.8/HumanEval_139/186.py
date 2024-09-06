
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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return n
    elif n == 3:
        return n * n
    elif n == 4:
        return n * n * n
    else:
        x = n
        factorial = 1
        while x >= 2:
            factorial *= x
            x -= 1
        return n * factorial
