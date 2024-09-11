```python
def memoize(func):
    """Decorator to cache function results"""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def fib(n: int):
    """
    Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memoized(n: int):
    """
    Return n-th Fibonacci number using memoization.
    >>> fib_memoized(10)
    55
    >>> fib_memoized(1)
    1
    >>> fib_memoized(8)
    21
    """
    memoized_fib = memoize(fib)
    return memoized_fib(n)


# Test the functions
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21

print(fib_memoized(10))  # Output: 55
print(fib_memoized(1))   # Output: 1
print(fib_memoized(8))   # Output: 21
```

In this code, we have implemented two versions of the `fib` function:

- `fib(n)`: calculates the `n-th` Fibonacci number without memoization, using recursion. However, this approach has a high time complexity due to repeated calculations.

- `fib_memoized(n)`: calculates the `n-th` Fibonacci number using memoization. Memoization is a technique where we store the results of expensive function calls so that we can reuse them when the same inputs occur again. We achieve this by decorating the `fib` function with a `memoize` decorator, which caches the results of previous function calls. This approach significantly reduces the time complexity of calculating Fibonacci numbers.