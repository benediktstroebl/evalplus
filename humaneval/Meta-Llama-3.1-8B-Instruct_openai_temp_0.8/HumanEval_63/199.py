### FibFib Number Sequence
#### Efficient Computation using Dynamic Programming

```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the desired element in the sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a list to store the sequence elements
        fibfib_sequence = [0, 0, 1] + [0]*(n-2)

        # Compute the sequence elements using dynamic programming
        for i in range(3, n+1):
            fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]

        return fibfib_sequence[n]

# Test cases
print(fibfib(1))   # Expected output: 0
print(fibfib(5))   # Expected output: 4
print(fibfib(8))   # Expected output: 24
```

This script defines a function `fibfib(n)` that efficiently computes the n-th element of the FibFib number sequence using dynamic programming. It first handles the base cases and then uses a list to store and compute the sequence elements iteratively.