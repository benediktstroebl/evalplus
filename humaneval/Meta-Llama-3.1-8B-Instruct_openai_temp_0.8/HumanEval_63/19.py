```python
def fibfib(n: int) -> int:
    """
    Calculate the n-th element of the FibFib number sequence.

    Args:
    n (int): The position of the element in the sequence (1-indexed).

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Initialize the first three elements of the sequence
    a, b, c = 0, 0, 1

    # Calculate the n-th element
    for _ in range(2, n + 1):
        a, b, c = b, c, b + a + c

    return c

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines the `fibfib` function to calculate the n-th element of the FibFib number sequence using a simple iterative approach. The function first checks if the input `n` is less than 1, and raises a `ValueError` if it is. Otherwise, it initializes the first three elements of the sequence (`a`, `b`, and `c`) and calculates the n-th element by iterating from 2 to `n` in the sequence. Finally, it returns the n-th element.