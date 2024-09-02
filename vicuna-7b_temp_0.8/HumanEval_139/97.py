
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
    # Define the recursive function that calculates the brazilian factorial
    def brazilian_factorial(n):
        if n == 0:
            return 1
        else:
            return n * brazilian_factorial(n-1)

    # Call the recursive function with the input value
    return brazilian_factorial(n)
