```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        memo = {0: 0, 1: 0, 2: 1}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses memoization to store previously computed values of the FibFib sequence, which greatly improves efficiency for large values of `n`.