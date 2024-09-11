### Fibonacci Number Calculator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

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

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script defines a recursive function `fib` that calculates the nth Fibonacci number. The calculation uses a simple iterative approach to avoid potential stack overflow issues with large values of n. The function includes a docstring with example usage and a brief description of the Fibonacci sequence.