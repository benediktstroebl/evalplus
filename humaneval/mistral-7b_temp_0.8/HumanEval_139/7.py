
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
    # 4! = 4 * 3 * 2 * 1
    # 3! = 3 * 2 * 1
    # 2! = 2 * 1
    # 1! = 1
    # 4! * 3! * 2! * 1!
    # 24 * 6 * 2 * 1
    # 288
    # PYTHON CODE
    # Use math.factorial to solve this
    # https://docs.python.org/3/library/functions.html#math.factorial

    import math

    if n == 0:
        return 1

    # factorial(n) * factorial(n-1) * factorial(n-2) * factorial(n-3) * ...
    # You can calculate factorial(n) and factorial(n-1) at the same time
    #   factorial(n) = factorial(n-1) * n
    #   factorial(n-1) = factorial(n-2) * (n-1
