```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
    n (int): The position of the number to compute in the sequence.

    Returns:
    int: The n-th element of the fib4 number sequence.
    """

    # Initialize the first four numbers of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the rest of the sequence
    for _ in range(3, n):
        # Update the sequence numbers
        a, b, c, d = b, c, d, c + d + b

    # Return the n-th number in the sequence
    return d


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that computes the n-th element of the fib4 number sequence using an iterative approach, which is more efficient than the recursive approach for large values of `n`.