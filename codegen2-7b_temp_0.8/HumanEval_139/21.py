
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
    try:
        n = int(n)
        if n < 0:
            raise ValueError
    except ValueError:
        print("Please, use a positive integer.")
        return

    return sum(factorial(i) for i in range(1, n+1))
