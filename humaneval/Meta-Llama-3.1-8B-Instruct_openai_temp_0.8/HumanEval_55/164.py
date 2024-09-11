```python
def memoize(func):
    """A decorator to memoize a function."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return memoized_func


@memoize
def fib(n: int):
    """Return n-th Fibonacci number.

    Fibonacci numbers are a series of numbers in which each number is the sum
    of the two preceding ones, usually starting with 0 and 1.

    Args:
        n: The index of the Fibonacci number to return.

    Returns:
        The n-th Fibonacci number.

    Examples:
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
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses memoization (a technique to store the results of expensive function calls) to optimize the Fibonacci function. This significantly improves the performance for larger inputs.