
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    dp = [0 for _ in range(n + 1)]

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i] += dp[i - 1]
            elif j == 9:
                dp[i] += dp[i - 1]
            else:
                dp[i] += dp[i - 1] - dp[i - 2]

    return dp[n]
