
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
    # If the input is 0 or less, return 1.
    if n <= 0:
        return 1
    # Else, return the input time the special factorial of the input - 1.
    else:
        return n * special_factorial(n - 1)

