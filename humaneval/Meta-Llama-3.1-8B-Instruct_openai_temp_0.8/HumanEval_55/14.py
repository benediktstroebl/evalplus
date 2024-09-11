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
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines the function `fib(n)` that calculates the n-th Fibonacci number. The Fibonacci sequence is defined as: 

- F(1) = 1
- F(2) = 1
- F(n) = F(n-1) + F(n-2) for n > 2

The script includes a docstring that describes the function, its arguments, return values, and provides examples of how to use it. It also includes a test section where it prints the results of calling the `fib(n)` function for n=10, n=1, and n=8. 

You can save this script to a file, for example `fibonacci.py`, and then run it using Python: `python fibonacci.py`