### Fibonacci Number Generator
#### Python Implementation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to be generated.

    Returns:
    int: The n-th Fibonacci number.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
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

This script defines a recursive function `fib(n)` to calculate the n-th Fibonacci number. It handles edge cases where `n` is 1, 2, or a negative integer. The `fib(n)` function iterates from 2 to `n` to compute the Fibonacci number.

This implementation uses a O(n) time complexity and O(1) space complexity, making it efficient for large values of `n`.