
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

    numerator = 1
    denominator = 1
    for number in range(1, n):
        numerator *= number
        denominator *= (number - 1)
    return numerator / denominator
