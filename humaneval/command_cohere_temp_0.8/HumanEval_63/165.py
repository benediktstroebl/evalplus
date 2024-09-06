```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This Python script defines a function called `fibfib` that calculates the n-th number in the FibFib sequence, which is a variation of the Fibonacci sequence. The function takes an integer `n` as input and uses a list `dp` to store the previously computed values of the sequence. It initializes `dp` with the first three numbers of the sequence (0, 0, and 1). Then, it iterates from 3 to `n`, where each iteration calculates the next number in the sequence by summing the previous three numbers. Finally, the function returns the n-th value from the `dp` list, which is the desired number in the FibFib sequence.