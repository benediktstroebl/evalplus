### Fibonacci Number Calculator
```markdown
### Overview
This script defines a function `fib(n)` that calculates the n-th Fibonacci number.

### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

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
        return fib(n-1) + fib(n-2)


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
### Notes
This implementation uses recursion to calculate the n-th Fibonacci number. However, this approach can be inefficient for large values of n due to the repeated calculations involved. For larger values, consider using an iterative approach or memoization to improve performance.
```