
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = [[0] * (10 ** n) for _ in range(n + 1)]
    dp[0][str(n)] = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # The number of n-digit positive integers starting with 1 and ending with 1 is the same as the number
            # of n-digit positive integers ending with 1 and starting with 1
            dp[i][j] = dp[j][i]
    return dp[n][n]
