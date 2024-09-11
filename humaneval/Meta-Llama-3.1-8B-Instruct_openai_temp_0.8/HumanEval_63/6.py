```python
def fibfib(n: int) -> int:
    """
    Calculates the n-th element of the FibFib number sequence.

    The FibFib number sequence is defined as follows:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fibfib_prev_prev_prev = 0  # Initialize previous three values
    fibfib_prev_prev = 0
    fibfib_prev = 1

    for _ in range(3, n + 1):
        # Calculate the next value in the sequence
        fibfib_next = fibfib_prev + fibfib_prev_prev + fibfib_prev_prev_prev
        
        # Update the previous values
        fibfib_prev_prev_prev = fibfib_prev_prev
        fibfib_prev_prev = fibfib_prev
        fibfib_prev = fibfib_next

    return fibfib_prev

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that calculates the n-th element of the FibFib number sequence. It initializes the first three values in the sequence and then iteratively calculates the next value in the sequence using a loop. The function raises a `ValueError` if `n` is a negative integer.

The example test cases at the end of the script demonstrate the correctness of the function by printing the values of `fibfib(1)`, `fibfib(5)`, and `fibfib(8)`.