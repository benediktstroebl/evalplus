### Fibonacci Number Calculation
#### A Python Script to Calculate the N-th Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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

This script uses a simple iterative approach to calculate the n-th Fibonacci number. It starts with the base cases for n = 1 and n = 2, and then iteratively calculates the next Fibonacci number using the previously calculated numbers. The function also includes a check to ensure that n is a positive integer.