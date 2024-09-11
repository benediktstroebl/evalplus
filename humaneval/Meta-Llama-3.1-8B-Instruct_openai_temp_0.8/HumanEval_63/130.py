```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the sequence.

    Returns:
        int: The n-th element of the sequence.

    Raises:
        ValueError: If n is a non-positive integer.
    """

    if n <= 0:
        raise ValueError("Input should be a positive integer.")

    # Precompute a list of the first n+1 elements in the sequence for memoization
    fibfib_sequence = [0, 0, 1] + [0]*(n-1)

    # Compute the sequence using a loop, memoizing the results where possible
    for i in range(3, n+1):
        fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]

    return fibfib_sequence[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that efficiently computes the n-th element of the FibFib number sequence. It uses a precomputed list to memoize the results where possible, reducing the computational complexity of the function from O(2^n) to O(n). The function also includes a test for non-positive input and raises a `ValueError` in such cases.