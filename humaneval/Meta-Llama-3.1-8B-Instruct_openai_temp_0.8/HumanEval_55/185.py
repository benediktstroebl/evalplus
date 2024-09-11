### Fibonacci Number Generator

Below is a Python script that uses a top-down approach with memoization to generate Fibonacci numbers efficiently.

```python
def memoize(func):
    """
    A decorator to memoize function results.
    """
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
    
    Fibonacci numbers are a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1. This function uses dynamic programming to efficiently calculate large Fibonacci numbers.
    
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
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script defines a `memoize` decorator that caches function results to prevent redundant calculations. The `fib` function uses this decorator to efficiently calculate Fibonacci numbers. The script also includes example usage and a test suite to demonstrate the function's correctness.