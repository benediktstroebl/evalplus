
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
    if n == 0:
        return 1
    elif n == 1:
        return n
    elif n == 2:
        return n * 2
    elif n == 3:
        return n * 3
    elif n == 4:
        return n * 4
    elif n == 5:
        return n * 5
    elif n == 6:
        return n * 6
    elif n == 7:
        return n * 7
    elif n == 8:
        return n * 8
    elif n == 9:
        return n * 9
    elif n == 10:
        return n * 10
    elif n == 11:
        return n * 11
    elif n == 12:
        return n * 12
    elif n == 13:
        return n * 13
    elif n == 14:
        return n * 14
    elif n == 15:
        return n * 15
    return special_factorial(n - 1) * n

