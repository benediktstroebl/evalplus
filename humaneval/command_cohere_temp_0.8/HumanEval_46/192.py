```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    return dp[n]
```

This script uses an array (`dp`) to store computed values of the Fib4 sequence, updated iteratively using a loop. This avoids the recursion called for in the original directive. 

The script solves the problem efficiently, avoiding recursion, and is compatible with the given tests. You can assign the `fib4` function to a variable like `f` and use it as follows:
```python
f = fib4
>>> f(5)
4
>>> f(6)
8
>>> f(7)
14
``` 
This allows you to compute the Fib4 value for any given n efficiently without the use of recursion.