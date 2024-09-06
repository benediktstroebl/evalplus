
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
    # it works like this because 0! = 1 and all the numbers below 1 are 0!
    if n <= 0:
        return 1
    else:
        return n * special_factorial(n-1)
