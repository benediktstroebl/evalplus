### Fibonacci Number Generator
#### Using Dynamic Programming for Efficient Computation

Here is a Python script that uses dynamic programming to efficiently compute the Fibonacci number at any given position `n`:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

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
    if n <= 1:
        return n
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next
    return fib_curr

# Test the function with example inputs
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script uses a loop to efficiently compute the Fibonacci number at position `n`. The time complexity of this solution is O(n), which is much faster than the naive recursive approach (O(2^n)) for large values of `n`.