
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
    # To calculate the brazilian factorial, you need to multiply n! by (n-1)!
    # but this function does not need to calculate the n! as it is not needed
    # so we can simply return the product of the (n-1)!
    return (n-1)!