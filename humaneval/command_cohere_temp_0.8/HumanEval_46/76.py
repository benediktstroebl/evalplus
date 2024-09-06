```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on a provided formula. It initializes a list `dp` with the base cases of the sequence, and then iteratively computes subsequent elements by summing the values from the last four steps. The resulting `dp` list contains the Fib4 values up to `n`, so simply returns the n-th value. The efficiency comes from the avoidance of repeated calculations through the use of the dynamic programming approach.  This passes the provided tests since it returns the correct values for `fib4(5)`, `fib4(6)`, and `fib4(7)`.