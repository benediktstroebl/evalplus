
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
    # Check if the input is a positive integer
    if n < 0 or not n % 1 == 0:
        return 0
    # Calculate the special factorial
    result = 1
    for i in range(1, n):
        result *= i
    return result
