```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This Python script defines a function called `fibfib` that calculates the n-th number in the FibFib sequence, which is similar to the Fibonacci sequence but with a recursive formula (`fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`). The script starts with an initialization list (`dp = [0, 0, 1]`) that sets up the first three values of the sequence (0, 0, and 1). It then iterates from 3 to `n` (the input value), where each iteration calculates the next value in the sequence by summing up the previous three values (`dp[i-1] + dp[i-2] + dp[i-3]`). Finally, the script returns the n-th value from the developed `dp` array.