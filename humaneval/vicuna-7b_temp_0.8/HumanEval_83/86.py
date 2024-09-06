
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = 0
    for i in range(n+1):
        dp += n//i if n//i > 0 else 1
    return dp
