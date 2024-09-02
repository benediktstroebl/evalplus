
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
    # Here is the list of the special factorials
    factorials = [1]

    # Helper function to avoid using the same variable in the
    # recursive recursion
    def helper(n):
        if n == 1:
            return 1
        else:
            return factorials[-1] * helper(n - 1)

    for idx in range(2, n + 1):
        factorials.append(helper(idx))

    return factorials[-1]

