
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
    # Implement the algorithm that calculates the brazilian factorial of n
    # This implementation uses the same formula as the one explained above
    # We multiply n! by (n-1)!*1! and get the result of the brazilian factorial
    result = n * (n - 1) * (n - 2) * ... * 1
    return result
