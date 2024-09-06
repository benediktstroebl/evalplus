
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[n] = 1
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if (j + 1) % 2 == 0:
                dp[j] += dp[i]
    return dp[n]

if __name__ == "__main__":
    n = int(input().strip())
    result = starts_one_ends(n)
    print(result)