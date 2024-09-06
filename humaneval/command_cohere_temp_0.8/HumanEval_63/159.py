```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This Python script defines a function called `fibfib` that calculates the n-th number in the FibFib sequence, which is a variant of the Fibonacci sequence. The function takes an integer `n` as input and uses a list `dp` to store the previously computed values of the sequence. It starts by initializing `dp` with the first three numbers in the sequence (0, 0, and 1). Then, in each iteration of the for loop, the function calculates the next number in the sequence by summing the last three numbers in the `dp` list, representing the current, previous, and second previous values in the sequence. This efficient approach allows the function to calculate the n-th number in the FibFib sequence in O(1) time complexity, as it only requires constant space to store the last three values of the sequence.