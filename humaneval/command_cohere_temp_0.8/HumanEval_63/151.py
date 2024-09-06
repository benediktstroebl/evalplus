```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th number in the FibFib sequence. It starts with the initial conditions of the sequence (fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1), and iteratively calculates the subsequent numbers using a deterministic pattern (fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)). The calculation employs a list (`dp`) to store the computed values, improving efficiency by avoiding redundant recursive calls.