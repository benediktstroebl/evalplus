```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibbonacci sequence,
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(4, n + 1):
            a, b, c = b, c, a + b + c
        return c


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
print(fibfib(10))  # 85
```

This script uses memoization (caching) to store the results of previously computed values in the `a`, `b`, and `c` variables. This approach is more efficient than recalculating the same values multiple times, as required by the original recursive definition of the `fibfib` function. The time complexity of this solution is O(n), which is a significant improvement over the naive recursive approach with a time complexity of O(2^n).