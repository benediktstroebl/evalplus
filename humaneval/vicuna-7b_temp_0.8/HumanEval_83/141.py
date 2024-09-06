
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n should be an odd number
    if n % 2 == 0:
        return 0

    # Using dp
    count = 0
    # dp[i][j] is the number of n-digit positive integers that start with j and end with i
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 1
    for j in range(2, n + 1):
        dp[0][j] = 1
        for k in range(2, n + 1):
            dp[k][j] = dp[k - 1][j - 1] + dp[k - 1][j]

    # Using memoization
    for i in range(n + 1):
        for j in range(2, n + 1):
            if j < i:
                count += dp[i][j]

    return count
