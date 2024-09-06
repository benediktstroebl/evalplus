
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

    # `special_factorial()` is recursive and the base case is `n == 1`
    if n == 1:
        return 1
    # If the input is not 1, we recursively call `special_factorial()` and
    # multiply by the previous result
    return n * special_factorial(n - 1)

