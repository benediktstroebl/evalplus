
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
    # Test the input with a simple check
    if n < 1 or n % 1 == 0:
        raise ValueError('Invalid input')

    # Build the expression
    expression = n
    while n > 1:
        expression *= (n - 1)
        n //= 1

    return expression
