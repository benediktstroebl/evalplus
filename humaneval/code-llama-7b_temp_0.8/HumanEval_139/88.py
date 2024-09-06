
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

    special = []
    num = n
    while num >= 1:
        special.append(factorial(num))
        num = num - 1

    res = 1
    for i in special:
        res = res * i

    return res
