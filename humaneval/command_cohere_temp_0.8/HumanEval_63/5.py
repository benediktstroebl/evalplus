```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This Python script defines a function called `fibfib` that uses a loop to generate a sequence of numbers that follows the FibFib sequence definition provided. The sequence starts with 0 for `n=0` and `n=1`, and then the sequence follows the pattern of each number being the sum of the previous 3 numbers (starting with the 3rd number). The loop iterates from 3 up to `n`, where `n` is the position of the desired number in the sequence. The generated numbers are stored in a list called `dp`. The function then returns the value at `dp[n]`, which will be the n-th number in the FibFib sequence. This algorithm is not efficient with a time complexity of O(n) since it recomputes values multiple times.