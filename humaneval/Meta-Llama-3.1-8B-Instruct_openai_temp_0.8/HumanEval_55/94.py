```python
def memoize(func):
    """A decorator to memoize the results of expensive function calls."""
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
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"fib({i}) = {fib(i)}")
```

This script defines a function `fib(n)` which calculates the n-th Fibonacci number using a recursive approach with memoization. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again, thus avoiding repeated calculations.

The `memoize` decorator is used to add memoization to the `fib` function. This makes the function much more efficient for large values of `n`, as it avoids redundant calculations.

When you run this script, it will print out the first 10 Fibonacci numbers.