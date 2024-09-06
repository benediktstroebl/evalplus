
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
    # The function uses a recursion and after n iterations, it should return
    # the product of n! * (n-1)! * ... * 1!
    return (n * (n-1) * (n-2) * ... * 1)
