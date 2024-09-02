
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
    # Check if the input is a positive integer
    if not (n >= 1):
        return 0

    # Calculate the special factorial using a recursive approach
    return n * special_factorial(n-1) * special_factorial(n-2) * ... * special_factorial(1)
