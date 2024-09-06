```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on a list of precomputed values and without using recursion. The `dp` list serves as a cache to store the computed values, updating itself in a loop and adding the sum of the previous four values to compute the next number in the sequence. This algorithm is iterative and avoids the potential stack-related challenges associated with recursive solutions.