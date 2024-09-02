
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
    # Return 1 if n is 0
    if n == 0:
        return 1
    # Return 1 if n is positive
    if n > 0:
        return n
    # Calculate the Brazilian factorial by multiplying the number with the
    # factors that are less than n
    factors = [1, 2]
    while len(factors) < n:
        factors.append(factors[len(factors)-1] * n)
    # Multiply the factors and return the result
    result = 1
    for factor in factors:
        result *= factor
    return result
