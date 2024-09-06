
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
    # The Brazilian factorial is defined as:
    # n! * (n-1)! * (n-2)! * ... * 1!
    # where n > 0
    # Using the formula for the gcd of two numbers, we can find the gcd of
    # n! and n, and then multiply by the gcd of (n-1)! and (n-2)! and so on.
    # This will give us the special factorial.
    return pow(n, 1) * pow(n-1, 1) * pow(n-2, 1) * ... * pow(2, 1) * pow(1, 1)
