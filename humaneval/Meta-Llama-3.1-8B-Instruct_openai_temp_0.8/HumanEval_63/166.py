```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is defined as follows:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n: The position of the number in the sequence.

    Returns:
        The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, b + c + a
        return c

# Test cases
print(fibfib(1))   # 0
print(fibfib(5))   # 4
print(fibfib(8))   # 24
```

This script uses memoization to store the values of `a`, `b`, and `c` in each iteration to avoid redundant calculations. It can efficiently compute the n-th element of the FibFib number sequence in O(n) time complexity.