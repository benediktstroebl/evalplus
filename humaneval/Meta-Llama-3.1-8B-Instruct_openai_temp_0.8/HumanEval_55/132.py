### Fibonacci Number Generator
#### Problem: Calculate the nth Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to generate.

    Returns:
        int: The nth Fibonacci number.

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
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script uses a loop to calculate the nth Fibonacci number. The time complexity is O(n), which is much more efficient than the naive recursive approach with a time complexity of O(2^n).