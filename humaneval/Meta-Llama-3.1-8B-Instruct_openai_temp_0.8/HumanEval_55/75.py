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

This Python script defines a function `fib(n)` that calculates the n-th Fibonacci number using a iterative approach. It checks if the input `n` is a positive integer, and raises a ValueError if it's not. The function then initializes two variables `a` and `b` with the first two Fibonacci numbers, and uses a loop to calculate the next Fibonacci numbers until it reaches the n-th number. Finally, it returns the n-th Fibonacci number. The script includes docstrings and examples to explain the function's behavior.