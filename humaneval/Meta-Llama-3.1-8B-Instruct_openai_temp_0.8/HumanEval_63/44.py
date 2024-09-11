```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number sequence to compute.

    Returns:
        int: The nth element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize the first three elements of the sequence
    a, b, c = 0, 0, 1

    # Compute the nth element using dynamic programming
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines the `fibfib` function, which efficiently computes the nth element of the FibFib number sequence using dynamic programming. The time complexity is O(n), and the space complexity is O(1). The function also includes input validation to ensure that n is a non-negative integer.