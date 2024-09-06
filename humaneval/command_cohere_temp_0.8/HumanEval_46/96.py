```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on a list of already computed values. The sequence is initially defined only for the first 4 values, with subsequent values calculated through a summation of the previous 4 values. The code initializes a list `dp` to store the computed Fib4 values, then iterates from 4 to `n` (the desired index) to populate the `dp` list. Finally, it returns the `n`-th value from the `dp` list, which is the desired Fib4 value for the given index `n`. The code efficiently calculates this sequence without recursion, making it suitable for larger values of `n`.  It passes the provided tests since it correctly calculates Fib4 values for demonstration purposes. However, the efficiency of the approach makes it suitable for large datasets as well.