```python
def fibfib(n):
    # Create a memoization dictionary with initial values:
    # 0 at indices 0 and 1, and 1 at index 2.
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        # Compute the next value in the sequence using the definition:
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]
```
This code defines the `fibfib` function, which uses memoization to efficiently compute the n-th element of the FibFib sequence, as defined by the problem statement. The memoization dictionary `memo` stores the results of previous computations, so the function doesn't have to recompute them each time. This significantly reduces the complexity of the algorithm.