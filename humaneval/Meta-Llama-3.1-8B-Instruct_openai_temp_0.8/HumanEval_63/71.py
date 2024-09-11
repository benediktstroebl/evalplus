```markdown
**FibFib Number Sequence Computation**
=====================================

The following Python script efficiently computes the n-th element of the FibFib number sequence.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the FibFib number to be computed.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n < 2:
        return 0
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

**Explanation**

The `fibfib` function uses a dictionary (`memo`) to store previously computed values. This approach, known as memoization, avoids redundant computations and significantly improves performance for large values of `n`.

The function first checks if `n` is less than 2 and returns 0 if true. For `n >= 2`, it initializes the `memo` dictionary with base cases (0, 1, and 2) and then computes the remaining values iteratively, storing them in the `memo` dictionary. Finally, it returns the value of `memo[n]`.

This implementation has a time complexity of O(n) due to the use of memoization, which is much more efficient than the naive recursive approach with a time complexity of O(3^n).