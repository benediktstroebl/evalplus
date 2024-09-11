### Fibonacci Number Calculator
#### A Python Script to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Calculate the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

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
print(fib(10))   # Output: 55
print(fib(1))    # Output: 1
print(fib(8))    # Output: 21
```

This script defines a function `fib(n)` that calculates the nth Fibonacci number using a simple iterative approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. It also includes example use cases and a test section to demonstrate the function's correctness.