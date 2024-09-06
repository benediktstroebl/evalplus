```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th value in the FibFib sequence. It starts with the initial conditions for the sequence (fibfib(0) == 0, fibfib(1) == 0, fibfib(2) == 1) and uses a deterministic algorithm to calculate subsequent values. The algorithm efficiently computes the n-th value by storing previously calculated values in the `dp` array, reducing the complexity to O(1) for each subsequent calculation.  This is achieved by using the recursive formula `fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.