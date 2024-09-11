```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Precompute and store the first three elements
        a, b, c = 0, 0, 1
        
        # Dynamic programming to compute the rest
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
print(fibfib(-1))  # Raises ValueError
print(fibfib(0))   # Output: 0
print(fibfib(2))   # Output: 1
```