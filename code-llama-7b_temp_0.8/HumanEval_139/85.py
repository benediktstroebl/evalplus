
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
    my_list = []
    while n > 0:
        my_list.append(n)
        n -= 1
    result = 1
    for i in my_list:
        result *= i
    return result
