```markdown
### FibFib Number Sequence Calculator
#### A Python Script to Compute the n-th Element of the FibFib Number Sequence

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Examples:
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n <= 1:
        return 0
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script uses memoization to store the results of expensive function calls and reuse them when the same inputs occur again. This approach significantly improves the performance of the function by avoiding redundant calculations.