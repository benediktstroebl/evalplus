```python
def fibfib(n: int) -> int:
    """
    Computes the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element in the sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is a negative integer.

    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines the `fibfib` function according to the given specification. It uses a loop to efficiently compute the n-th element of the FibFib number sequence by maintaining a running sum of the last three elements. It also includes test cases to verify the function's correctness.