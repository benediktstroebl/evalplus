```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c + d
        return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function that computes the nth element of the Fib4 number sequence. It uses a bottom-up dynamic programming approach to store the last four elements of the sequence and compute the next element by summing the four previous elements. The function handles the base cases where `n` is 0, 1, 2, or 3 and returns the corresponding value.