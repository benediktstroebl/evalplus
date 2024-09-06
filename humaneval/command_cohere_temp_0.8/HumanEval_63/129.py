```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th value in the FibFib sequence. It does this by using a 3-step recursive approach, and then using a list (dp) to store already calculated values to avoid recalculation, thus making the approach linear time and O(n) where n is the index of the value being calculated. 

This approach guarantees a consistent and efficient solution for calculating the FibFib values.