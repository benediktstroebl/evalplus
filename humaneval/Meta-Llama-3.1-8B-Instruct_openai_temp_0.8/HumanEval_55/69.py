```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.

    Examples:
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
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python script defines the function `fib(n)` that returns the n-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci number for larger n efficiently. If n is not a positive integer, it raises a `ValueError`.

The function is then tested with the provided examples to demonstrate its correctness.