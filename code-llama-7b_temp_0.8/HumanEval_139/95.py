
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
    # Keep track of a list of the results so far:
    results = [1]
    while len(results) <= n:
        # Pop the last result from the list, multiply it by all previous results
        # and add the result to the list of results:
        result = results.pop() * len(results)
        results.append(result)
    return results[-1]
