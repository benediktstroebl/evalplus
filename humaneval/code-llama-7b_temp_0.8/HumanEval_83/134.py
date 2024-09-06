
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def helper(n, k):
        if n == 0:
            return 0
        elif n == 1:
            return 2
        else:
            return 2 * k * (9 ** n) + helper(n - 1, k * 10)
    
    return helper(n, 1) + helper(n, 2)

