
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
    # If n is positive
    if n > 0:
        # Compute all the factorials
        result = n
        for i in range(1, n+1):
            result *= (i + 1)
        return result
    # If n is zero
    elif n == 0:
        return 1
    # If n is negative
    else:
        return -1 #can't return negative value in python
