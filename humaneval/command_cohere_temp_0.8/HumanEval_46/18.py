```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(5, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]
```
This code defines a function `fib4` that uses dynamic programming to compute the n-th element of the Fib4 sequence, which is defined as follows:
- `fib4(0) -> 0`
- `fib4(1) -> 0`
- `fib4(2) -> 2`
- `fib4(3) -> 0`
- `fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

The function initializes a list `dp` with the base cases and then fills it up with the calculated values for `fib4(n)` using a loop, checking each value once. It then returns `dp[n]`, which will be the n-th element in the Fib4 sequence.