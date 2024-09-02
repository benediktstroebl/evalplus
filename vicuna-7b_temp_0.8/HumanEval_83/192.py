
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    elif n < 5:
        return n
    else:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i]
        return dp[-1]

