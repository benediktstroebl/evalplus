```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the sequence to compute.
    
    Returns:
    int: The nth element of the fibfib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Use memoization to store previously computed values
        memo = {0: 0, 1: 0, 2: 1}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses memoization to efficiently compute the nth element of the fibfib number sequence. It stores the computed values in a dictionary `memo` and reuses them instead of recomputing them. This approach reduces the time complexity from exponential to linear.