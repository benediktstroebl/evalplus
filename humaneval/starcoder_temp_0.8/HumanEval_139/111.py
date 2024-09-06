
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
    # # Solution using math module
    # return math.factorial(n) * math.prod(
    #     [math.factorial(n - i - 1) for i in range(n - 1)]
    # )

    # Solution without using math module
    if n <= 0:
        return 1
    else:
        return n * special_factorial(n - 1)

