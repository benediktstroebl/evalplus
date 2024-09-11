```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the sequence to compute.

    Returns:
        int: The n-th element of the fib4 number sequence.

    Raises:
        ValueError: If n is a negative integer.

    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize the first four elements of the sequence
        a, b, c, d = 0, 0, 2, 0

        # Compute the rest of the sequence
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c + d

        return d

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses an iterative approach to compute the n-th element of the fib4 number sequence. It initializes the first four elements of the sequence and then iteratively updates the elements to compute the rest of the sequence. This approach avoids the need for recursive function calls and is more efficient for large values of n.