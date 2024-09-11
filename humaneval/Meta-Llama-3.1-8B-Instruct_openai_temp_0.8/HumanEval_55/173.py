### Fibonacci Number Calculation

Below is a Python script that calculates the `n`-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number.

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

This script uses an iterative approach to calculate the `n`-th Fibonacci number. It starts by checking for the base cases where `n` is 1 or 2. For larger values of `n`, it uses a loop to calculate the Fibonacci number. This approach is more efficient than a recursive approach, especially for larger values of `n`.