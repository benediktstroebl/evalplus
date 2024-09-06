
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def helper(n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        return helper(n-1) + helper(n-2)
    
    return helper(n)
