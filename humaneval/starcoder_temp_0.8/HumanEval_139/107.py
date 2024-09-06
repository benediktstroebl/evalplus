
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
    # if 1 or 0 factorial is 1
    if n <= 1:
        return 1
    # if negative number return 0
    if n < 0:
        return 0
    # if number is greater or equal than 10 return 0
    if n >= 10:
        return 0
    # return the sum of the factorial of the given integer and the factorial
    # of each number between 1 and the integer - 1.
    return n * factorial(n - 1)
