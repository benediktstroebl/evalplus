
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
    specials = [1]

    if n > 1:
        n_minus_one = n - 1
        for i in range(2, n_minus_one + 1):
            specials.append(i * specials[-1])

    return reduce(lambda x, y: x * y, specials)
