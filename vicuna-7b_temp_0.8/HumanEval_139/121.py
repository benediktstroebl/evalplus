
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
    # A generator is a function that yields values.
    def gen():
        for i in range(1, n+1):
            yield i

    # The generator is used to compute the special factorial using the
    # definition above.
    for i in gen():
        n *= i

    return n
