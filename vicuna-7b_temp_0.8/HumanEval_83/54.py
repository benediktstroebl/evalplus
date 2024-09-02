
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i][0] = i
        for j in range(i):
            dp[i][j + 1] = dp[i - 1][j]
    return dp[n][n]

print(starts_one_ends(5))  # prints 2