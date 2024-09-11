```python
def memoize(func):
    """A decorator function to store the results of expensive function calls and return the cached result when the same inputs occur again."""
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
    """
    Return n-th Fibonacci number.

    This function uses memoization to improve performance for large inputs.
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
if __name__ == "__main__":
    print(fib(10))  # 55
    print(fib(1))   # 1
    print(fib(8))   # 21
```

This script defines a `fib` function that returns the n-th Fibonacci number. The `fib` function uses a decorator called `memoize` to improve its performance by caching the results of expensive function calls. This way, when the function is called with the same input multiple times, it can return the cached result instead of recalculating it. This can significantly improve performance for large inputs. The script also includes docstrings and test cases to demonstrate its usage.