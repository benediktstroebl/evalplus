```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting from 0 and 1. This function implements an iterative approach to calculate the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number. It handles edge cases where `n` is less than or equal to 0, and uses an iterative approach to efficiently calculate the Fibonacci number for larger values of `n`. The function includes docstrings that provide explanations and usage examples, following standard Python documentation conventions.