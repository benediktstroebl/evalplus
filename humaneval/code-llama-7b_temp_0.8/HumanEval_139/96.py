
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
    list_int = []
    n_factorial = 1
    factorial = 1
    for i in range(1,n+1):
        list_int.append(i)
    for i in list_int:
        for j in range(1, i+1):
            factorial = factorial * j
        n_factorial = n_factorial * factorial
    return n_factorial
