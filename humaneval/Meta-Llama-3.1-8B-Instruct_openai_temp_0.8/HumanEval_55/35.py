### Fibonacci Number Generator
#### Using Memoization for Efficiency

```python
def memoize(func):
    """Decorator to memoize function results."""
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

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.

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


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

In this code:

*   The `memoize` function is a decorator used to memoize function results. It caches the results of the function calls to avoid redundant calculations.
*   The `fib` function uses the `memoize` decorator to efficiently generate Fibonacci numbers. It takes advantage of the memoized results by using recursive function calls with cached values.
*   The docstring of the `fib` function includes an example usage section with doctests to verify its correctness.
*   The code includes a clear example usage section at the end to demonstrate how to use the `fib` function.

This script provides an efficient solution to generate Fibonacci numbers using memoization, reducing the time complexity of the recursive function calls.