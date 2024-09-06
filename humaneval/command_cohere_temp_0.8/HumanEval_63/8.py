```python
def fibfib(n: int):
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This code defines a function `fibfib` that efficiently calculates the n-th number in the FibFib sequence. The sequence is initialized with the base cases (`fibfib(0) == 0` and `fibfib(1) == 0`) and then each subsequent number is computed as the sum of the three previous numbers in the sequence, up to the n-th number.

The code uses a discrete process to efficiently calculate the numbers, storing them in a list (`dp`) to avoid recomputation, and linearly runs through the list from 3 to `n`, calculating each number in the sequence. This is an efficient way to calculate these numbers, especially as the size of n grows. 

The given tests demonstrate the correctness and efficiency of the function. 
```python
# Tests
assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24
``` 
The first test checks the initial conditions of the FibFib sequence, the second test checks a value in the middle of the sequence and the third test checks a value towards the end of the sequence.  feedback provided by the tests helps to confirm the correctness of the implementation.  This type of dynamic programming problem is efficient because it avoids redundant calculations, making it a good approach for this type of sequence.