```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
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
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize variables to store the last three numbers in the sequence
    a, b, c = 0, 0, 1

    # Compute the n-th number in the sequence
    for _ in range(3, n + 1):
        # Update a, b, and c to the next three numbers in the sequence
        a, b, c = b, c, a + b + c

    return c


# Test the function
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This Python script implements the `fibfib` function, which efficiently computes the n-th element of the FibFib number sequence using a bottom-up dynamic programming approach. The function takes an integer `n` as input and returns the corresponding FibFib number. It also includes base cases and error handling for negative input values.