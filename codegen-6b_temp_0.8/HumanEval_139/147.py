
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
    # We use the below factorial formula for calculating the factorial value.
    # Factorial is the product of all numbers until a particular
    # number (denoted as n)
    # Factorial of a number (n) is:
    # 1! = 1
    # n! = (n-1)! * n
    # where n > 0
    factorial = 1
    for num in range(2, n+1):
        factorial *= num
    return factorial
