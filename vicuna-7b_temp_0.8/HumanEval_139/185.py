
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
    # Algorithm to calculate the brazilian factorial
    # The formula is n! * (n-1)! * (n-2)! * ... * 1!
    # It is calculated by repeatedly multiplying the previous number by the current number,
    # and at the same time subtracting 1 from the current number
    # The final result is returned
    if n == 0:
        return 1
    else:
        return (n * special_factorial(n-1)) / 2