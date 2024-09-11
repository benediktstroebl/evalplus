### Fibonacci Series Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to generate.

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
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This Python script defines a function `fib(n)` that generates the `n-th` Fibonacci number. It uses an iterative approach to calculate the Fibonacci number, which is more efficient than a recursive approach for large values of `n`. The function also includes docstrings to provide documentation and examples of usage.