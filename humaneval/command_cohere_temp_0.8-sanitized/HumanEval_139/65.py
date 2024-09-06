def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288
    """
    factorial_product = 1
    for i in range(2, n+1):
        factorial_product *= i
    return factorial_product