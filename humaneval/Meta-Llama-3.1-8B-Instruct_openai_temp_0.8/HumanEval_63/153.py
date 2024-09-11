```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the sequence to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        # Use memoization to store previously computed values
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that uses memoization to efficiently compute the n-th element of the FibFib number sequence. Memoization is a technique where we store previously computed values in a dictionary to avoid redundant computations. The time complexity of this function is O(n), which is much faster than the naive recursive approach which has a time complexity of O(3^n) due to the repeated computations.