
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def helper(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        return helper(n-1) + (n-1)*9*10**(n-2)
    return helper(n)
