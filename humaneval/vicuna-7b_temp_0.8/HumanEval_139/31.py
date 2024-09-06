
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
    # You can use the same solution as the given one.
    # The time complexity of this solution is O(n!) and the space complexity is O(n)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result