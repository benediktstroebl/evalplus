### Efficient Implementation of the Fib4 Sequence
#### Using Dynamic Programming for Memoization

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position in the sequence to compute.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize the base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize a list to store the sequence
    fib4_sequence = [0] * (n + 1)
    
    # Compute the first four elements of the sequence
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    if n >= 3:
        fib4_sequence[3] = 0
    
    # Compute the rest of the sequence
    for i in range(4, n + 1):
        # Use the recurrence relation to compute the next element
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
    
    # Return the n-th element of the sequence
    return fib4_sequence[n]
```

This script efficiently computes the n-th element of the Fib4 number sequence using dynamic programming with memoization. It initializes the base cases and then uses a loop to compute the rest of the sequence. The recurrence relation is applied to compute each element, and the result is returned at the end.