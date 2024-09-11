### FibFib Number Sequence
#### Python Script to Compute the `n`-th Element

```python
def fibfib(n: int) -> int:
    """
    Compute the `n`-th element of the FibFib number sequence.

    The FibFib number sequence is defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n: A non-negative integer.

    Returns:
        The `n`-th element of the FibFib number sequence.

    Raises:
        ValueError: If `n` is a negative integer.

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Compute the `n`-th element using dynamic programming
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Example usage
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This Python script defines a function `fibfib(n)` to compute the `n`-th element of the FibFib number sequence using dynamic programming. It also includes example usage and input validation.