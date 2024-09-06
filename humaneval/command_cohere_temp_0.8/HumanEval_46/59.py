```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    return dp[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on the formula for Fib4. The code initializes a list `dp` with the first four values of the Fib4 sequence. It then iteratively computes the subsequent Fib4 values and stores them in the `dp` list. Finally, the function returns the n-th value from the `dp` list, accurately computing the Fib4 value for any given n. This approach ensures efficiency and avoids recursion, achieving a time complexity of O(n) for calculating each Fib4 value.