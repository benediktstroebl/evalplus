```python
def fib4(n: int) -> int:
    dp = [0, 0, 2, 0]
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    return dp[n]
```

This script uses an array (`dp`) to store previously computed values of the Fib4 sequence. It then iteratively updates the array using a loop, where each element of the sequence is the sum of the previous four elements. This avoids the recursion called for in the task request. 

This approach has a time complexity of O(n) since each value is computed only once and stored in the array, and each value retrieval only requires a constant amount of time.

The given tests pass with this code, as the function correctly computes the Fib4 number for any input `n`. 
```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
``` 
This output confirms that the script produces the correct Fib4 values for these test cases.