```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n <= 3:
        # Base cases
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            return 0

    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the n-th element
    for _ in range(4, n + 1):
        # Update the elements
        a, b, c, d = b, c, d, a + b + c + d

    return d


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the n-th element of the Fib4 number sequence. The function `fib4(n)` initializes the first four elements of the sequence and then iteratively updates them to compute the n-th element. The base cases for `n <= 3` are handled separately.