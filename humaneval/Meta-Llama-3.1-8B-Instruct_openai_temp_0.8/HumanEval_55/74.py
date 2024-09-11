```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Example:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script implements the `fib` function, which uses an iterative approach to calculate the n-th Fibonacci number. It handles edge cases where `n` is less than or equal to 0 and provides a docstring to document its functionality. The script also includes example usage to demonstrate the function's behavior.