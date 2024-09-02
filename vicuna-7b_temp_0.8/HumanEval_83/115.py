
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case: if n < 10, return 1
    if n < 10:
        return 1
    
    # use dynamic programming approach
    # using a two-dimensional array dp
    dp = [[0] * (10 ** n) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # for each digit in the number
    for i in range(1, n + 1):
        # for each digit in the number
        for j in range(1, n + 1):
            # for each way the number can be written as n-digit number
            # where the first digit is i and the last digit is j
            for k in range(1, n + 1):
                # add up the counts
                dp[i][j] += dp[i][k]
    
    return dp[n][n]