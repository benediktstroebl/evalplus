
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
    # factorial of the last term of the Brazilian factorial
    last_term_factorial = (n-1) * special_factorial(n-1) * special_factorial(n-2) * special_factorial(n-3) * ... * special_factorial(1)

    # multiply all the other terms of the brazilian factorial
    brazilian_factorial = n * last_term_factorial

    return brazilian_factorial
