### Fibonacci Number Generator
#### A Python Script to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    Fibonacci sequence is defined as:
    - F(1) = 1
    - F(2) = 1
    - For n > 2, F(n) = F(n-1) + F(n-2)

    Example use cases:
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
        return fib(n-1) + fib(n-2)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python script uses a recursive approach to calculate the nth Fibonacci number. However, please note that this approach is not efficient for large values of `n` due to the repeated calculations involved. For larger values of `n`, consider using an iterative approach or memoization to improve performance.

### Iterative Alternative
If you prefer an iterative solution, you can use the following implementation:

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    fib_prev = 1
    fib_curr = 1
    
    for _ in range(3, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This iterative approach avoids the repeated calculations involved in the recursive solution, making it more efficient for large values of `n`.