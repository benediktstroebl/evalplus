```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n: A non-negative integer.

    Returns:
        The nth element of the FibFib sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script efficiently computes the nth element of the FibFib sequence by using a bottom-up dynamic programming approach. It initializes three variables `a`, `b`, and `c` to the first three elements of the sequence (0, 0, and 1). Then it iterates from 3 to `n` (inclusive) and updates `a`, `b`, and `c` to the next three elements of the sequence. The script finally returns `c`, which is the nth element of the FibFib sequence.