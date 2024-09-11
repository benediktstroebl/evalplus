```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the number in the FibFib sequence.

    Returns:
    int: The n-th number in the FibFib sequence.

    Example:
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Array to store the sequence
        sequence = [0, 0, 1]
        for i in range(3, n + 1):
            # Calculate the next number as the sum of the previous three numbers
            next_number = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            sequence.append(next_number)
        return sequence[n]

# Test the function
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This script defines a function `fibfib(n)` to compute the n-th number in the FibFib sequence. It uses a loop to build up the sequence from the first three numbers (0, 0, 1) to the n-th number. This approach has a time complexity of O(n), making it efficient for large values of n.