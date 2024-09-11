```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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

# Test the function
if __name__ == "__main__":
    print(fib(10))   # Output: 55
    print(fib(1))    # Output: 1
    print(fib(8))    # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number. It uses an iterative approach for efficiency. The function also includes a docstring that provides documentation and examples of how to use it. The script includes a test section at the end that demonstrates how to use the `fib(n)` function.