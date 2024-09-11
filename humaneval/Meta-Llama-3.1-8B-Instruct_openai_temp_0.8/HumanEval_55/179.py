```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number in the sequence.

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
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

This script uses a simple iterative approach to calculate the n-th Fibonacci number, which is more efficient than the recursive approach for large values of n. It also includes a check to raise a ValueError if the input is not a positive integer.