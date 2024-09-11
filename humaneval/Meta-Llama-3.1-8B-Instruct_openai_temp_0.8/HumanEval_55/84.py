### Fibonacci Function in Python
```python
def memoize(func):
    """Memoization decorator to store and reuse function results."""
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
    return fib(n-1) + fib(n-2)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
    print(fib(20))  # Output: 6765
```
This script defines a `fib` function that returns the `n-th` Fibonacci number using memoization to optimize performance for larger inputs.

The `memoize` decorator stores the results of function calls to avoid redundant computations. This approach significantly improves the function's efficiency for large inputs.

The provided example usage demonstrates the function's effectiveness with various inputs.