```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th number in the FibFib sequence. It starts with the base cases (`fibfib(0) == 0`, `fibfib(1) == 0`, `fibfib(2) == 1`) and iteratively computes subsequent elements using a loop, updating the values in the `dp` array. The resulting array `dp` contains the computed FibFib values up to `n`. Therefore, the function `fibfib(n)` returns the n-th number in the FibFib sequence.