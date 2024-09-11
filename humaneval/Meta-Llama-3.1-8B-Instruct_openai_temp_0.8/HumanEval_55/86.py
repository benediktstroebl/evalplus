### Fibonacci Number Calculator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

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
        for _ in range(n - 2):
            a, b = b, a + b
        return b


# Test the function
print(fib(10))   # Output: 55
print(fib(1))    # Output: 1
print(fib(8))    # Output: 21
```
This script defines a `fib` function that calculates the n-th Fibonacci number using a simple iterative approach. It includes docstrings and example use cases to demonstrate its usage. The function raises a `ValueError` if the input `n` is not a positive integer.