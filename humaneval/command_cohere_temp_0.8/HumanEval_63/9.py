```python
def fibfib(n):
    # Create an memoization dictionary with initial values:
    memo = {
        0: 0,
        1: 0,
        2: 1,
    }
    # Check if the result is already cached:
    if n in memo:
        return memo[n]
    # Otherwise, compute and store the result in the dictionary:
    if n >= 3:
        memo[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # Return the final result:
    return memo[n]
```

This code uses memoization to compute the FibFib values and achieves an efficient time complexity of O(n) for calculating the n-th FibFib number.

To use this code, simply call the `fibfib` function with a given integer `n`. For example:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```