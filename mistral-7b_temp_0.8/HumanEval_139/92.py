
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
    # TODO: Replace this line with your code
    # return (1,) + (n,) * n
    num = n
    while num > 0:
        num = num - 1
        factorial = (num,) + (n,) * num
        num = num - 1
    return factorial

