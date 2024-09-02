
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

    # If n < 0, then return 0
    if n < 0:
        return 0

    # Initialize a list to store the results of the recursive calls
    results = []

    # Take a look at this function definition below:
    # def factorial(n):
    #     if n == 0:
    #         return 1
    #     else:
    #         return n * factorial(n-1)
    #
    # Note that in order to use this recursive function, we need to change the
    # factorial function to have an extra argument:
    # def factorial(n, results):
    #     if n == 0:
    #         results.append(1)
    #         return 1
    #     else:
    #         results.append(n)
    #         return n * factorial(n-1, results)
    #
    # The extra argument 'results' will be a list that will store the values
    # of all the recursive calls to the function. The results of the calls
    # are appended to this list.

    def factorial(n, results):
        if n == 0:
            results.append(1)
            return 1
        else:
            results.append(n)
            return n * factorial(n-1, results)

    return factorial(n, results) * reduce(lambda x, y: x*y, results[1:], 1)

