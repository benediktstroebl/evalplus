### Fibonacci Number Generator
#### Using Dynamic Programming for Efficiency
```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

    Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

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
    else:
        fib_prev, fib_curr = 0, 1
        for _ in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev, fib_curr = fib_curr, fib_next
        return fib_curr

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script generates Fibonacci numbers using dynamic programming for efficiency, especially for larger values of `n`. It uses a simple iterative approach to calculate the `n`-th Fibonacci number in `O(n)` time complexity.