```python
def memoize(func):
    """Decorator function to cache results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

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
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script calculates the `n`-th Fibonacci number using a memoized approach. This approach stores the results of expensive function calls so that they can be reused when the same inputs occur again. This significantly improves the performance for large values of `n`. 

The script defines a decorator function `memoize` that implements this caching behavior. The `fib` function is then decorated with `memoize` to enable memoization. The `fib` function itself uses a simple recursive approach to calculate the `n`-th Fibonacci number. If `n` is less than or equal to 2, it returns 1; otherwise, it returns the sum of the `(n-1)`-th and `(n-2)`-th Fibonacci numbers.