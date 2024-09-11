### Fibonacci-like Sequence (FibFib)
#### Self-Contained Python Script

```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the FibFib sequence.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


# Example use cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that calculates the `n`-th element of the FibFib sequence. It uses a simple iterative approach to improve performance. The function also includes input validation to raise a `ValueError` for negative integers. The example use cases demonstrate the function's usage and expected output.