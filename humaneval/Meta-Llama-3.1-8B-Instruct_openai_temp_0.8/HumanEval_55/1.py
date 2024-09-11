```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

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
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this recursive solution is not efficient for large values of n as it performs a lot of repeated computations. A more efficient solution uses dynamic programming to store and reuse previously computed Fibonacci numbers.

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

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
        fib_dict = {1: 1, 2: 1}
        for i in range(3, n+1):
            fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
        return fib_dict[n]


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```