```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n <= 3:
        return 0

    # Initialize the array to store the sequence
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0

    # Compute the sequence iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]

    return fib4_sequence[n]
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the Fib4 number sequence using dynamic programming. It uses an array to store the sequence and computes each element iteratively. The function handles non-negative integer indices and raises a `ValueError` for negative indices.