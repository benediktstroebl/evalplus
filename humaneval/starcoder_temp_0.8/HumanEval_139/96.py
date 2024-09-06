
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
    # make sure n is a positive integer
    assert isinstance(n, int), "n must be an integer."
    assert n > 0, "n must be a positive integer."

    # implement the special factorial function
    special = 1
    for i in range(1, n+1):
        special = special * i
    return special
