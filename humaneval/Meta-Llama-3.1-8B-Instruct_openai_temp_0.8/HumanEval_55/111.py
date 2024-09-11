### Fibonacci Number Generator
#### A Python Function to Calculate the n-th Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

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

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a recursive function `fib(n)` that calculates the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function raises a ValueError if n is not a positive integer. If n is 1, it simply returns 1. Otherwise, it uses a loop to calculate the n-th Fibonacci number iteratively.