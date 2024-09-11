```python
def memoize(func):
    """Memoization decorator to store the results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Example usage
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses a decorator called `memoize` to optimize the `fib` function. The `memoize` function stores the results of the `fib` function to avoid redundant calculations. This makes the `fib` function much more efficient for large inputs.