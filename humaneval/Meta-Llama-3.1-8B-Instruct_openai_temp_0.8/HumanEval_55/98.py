```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
    
    Args:
    n (int): The index of the Fibonacci number to return.
    
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

This script uses an iterative approach to calculate the n-th Fibonacci number, which is more efficient than the recursive approach for larger values of n. The function raises a ValueError if n is not a positive integer.