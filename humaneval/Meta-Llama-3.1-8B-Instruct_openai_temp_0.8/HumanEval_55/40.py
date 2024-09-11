```python
def memoize(func):
    """Decorator to cache the results of expensive function calls."""
    cache = dict()

    def memoized_func(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return memoized_func


@memoize
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a technique called memoization to store the results of expensive function calls and reuse them when the same inputs occur again. This makes the function much more efficient for large values of `n`.

The `memoize` decorator creates a cache to store the results of function calls, and the `fib` function uses this decorator to store and reuse its results. The `fib` function then becomes much faster for large values of `n` because it avoids redundant function calls.