
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
    def recursion(n):
        if n == 1 or n == 0:
            return 1
        return n * recursion(n - 1)
    if n <= 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= recursion(i)
    return result

