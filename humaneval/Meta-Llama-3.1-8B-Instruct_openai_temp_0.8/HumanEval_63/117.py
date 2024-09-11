```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.

    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c


# Test the function
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script defines a function `fibfib` that efficiently computes the n-th element of the FibFib number sequence. It first checks for invalid input (negative n), and then uses a loop to calculate the sequence up to the n-th element. The function then returns the n-th element.

The script includes docstrings and example use cases to demonstrate the function's usage.