
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
    # Just in case it's not a positive integer, return 1
    if n < 0:
        return 1
    # Calculate the sum of the terms
    sum_of_terms = (n * (n-1) * (n-2) * ... * 1)
    # Multiply the sum by the number of terms
    return sum_of_terms * (n-1) * (n-2) * ... * 1
