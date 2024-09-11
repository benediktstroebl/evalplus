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

This script defines a function `fib(n)` that calculates the `n`-th Fibonacci number. The function uses a loop to calculate the Fibonacci numbers iteratively, which is more efficient than recursive methods for large values of `n`. It also includes error checking to ensure that `n` is a positive integer. The script includes example use cases and test the function with various inputs.