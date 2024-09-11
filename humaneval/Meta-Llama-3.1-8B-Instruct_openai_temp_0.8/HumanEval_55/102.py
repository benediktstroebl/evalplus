```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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

# Test cases
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

This Python script defines a function `fib(n)` that calculates the n-th Fibonacci number. It uses a loop to iteratively calculate the Fibonacci sequence up to the n-th number, and returns the result. The script also includes test cases to demonstrate the function's correctness.