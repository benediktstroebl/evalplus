```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th number in the FibFib sequence. The sequence is initialized with the base cases (`fibfib(0) == 0` and `fibfib(1) == 0`) and then iteratively defines each number as the sum of the previous 3 elements in the sequence, starting from the 3rd element.

The script uses a list `dp` to store the computed values of the FibFib sequence. It starts with `dp[0]` and `dp[1]` set to 0, reflecting the initial base cases. Subsequently, the element at position `i` is computed as the sum of the elements at positions `i-1`, `i-2`, and `i-3`, reflecting the definition of the FibFib sequence.

This approach ensures efficiency as it calculates each subsequent element of the sequence only once, reusing the computed values to arrive at the final result for `dp[n]`. The script showcases an optimized approach to solving this problem, avoiding repeated calculations and leveraging the intrinsic nature of the sequence's definition.