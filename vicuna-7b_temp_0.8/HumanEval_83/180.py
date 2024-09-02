
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[n] = 1
    for i in range(1, n):
        dp[i] = dp[i-1] + dp[i]
    return dp[n-1]
