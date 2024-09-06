def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(5, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]