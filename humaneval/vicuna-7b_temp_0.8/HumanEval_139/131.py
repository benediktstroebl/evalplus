
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
    # The special factorial of 0 is 1
    if n == 0:
        return 1

    # The special factorial of any other integer is the product of all the integers
    # from 1 to that integer (excluding 1)
    product = 1
    for i in range(1, n+1):
        product *= i
    return product
