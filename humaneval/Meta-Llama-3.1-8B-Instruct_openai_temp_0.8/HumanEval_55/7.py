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
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this recursive implementation has a time complexity of O(2^n), which is not efficient for large values of n. Here's an iterative approach:

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
    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This iterative version has a time complexity of O(n), making it much more efficient for large values of n.