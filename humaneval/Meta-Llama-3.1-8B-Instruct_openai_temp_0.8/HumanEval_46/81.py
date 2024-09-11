```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.

    Args:
        n (int): The position of the element in the fib4 sequence to compute.

    Returns:
        int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the rest of the sequence
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d


# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the Fib4 number sequence. The function uses a loop to compute the sequence iteratively, avoiding the use of recursion. It handles edge cases for n <= 3 separately and then uses a loop to compute the rest of the sequence. The function returns the n-th element of the sequence.