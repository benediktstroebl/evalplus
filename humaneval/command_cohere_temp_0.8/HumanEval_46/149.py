```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    return dp[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on a given n. It initializes a list dp with the first four numbers in the sequence. Then, it iterates through the elements from 4 to n, appending the sum of the previous four numbers in the sequence to the dp list. This way, each value in the list dp is the sum of the previous four numbers, effectively calculating the Fib4 sequence. The function returns the n-th value in the sequence, which is the value stored at index n in the dp list.