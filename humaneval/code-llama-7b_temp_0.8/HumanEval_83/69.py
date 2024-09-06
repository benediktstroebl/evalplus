
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def f(n, b):
        return 10**n - b
    return (f(n,1) + f(n,9))
