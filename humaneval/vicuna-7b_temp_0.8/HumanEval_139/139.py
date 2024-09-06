
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
    if n < 0 or n == 0:
        raise ValueError("The input should be a non-negative integer.")

    factors = [1]
    i = 2

    while i <= n:
        if i % 2 == 0:
            factors.append(i)
        i += 1

    factors.reverse()
    result = 1

    for factor in factors:
        result *= factor

    return result
