```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence 
    without using recursion.

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    a, b, c, d = 0, 0, 2, 0

    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d
```

You can test this function with the provided examples:
```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the n-th element of the fib4 number sequence. It initializes the first four elements of the sequence (a, b, c, d) and then iteratively updates them to compute the subsequent elements. The function returns the n-th element of the sequence.