
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def f(n):
        if n == 1:
            return 1
        return f(n-1) + f(n-1) + 1
    return f(n)

