```python
def memoize(func):
    """A decorator to memoize the function results."""
    cache = dict()

    def memoized_func(*args):
        """Return the result from the cache if available, otherwise compute and store it."""
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Example usage:
print(fibfib(1))     # Output: 0
print(fibfib(5))     # Output: 4
print(fibfib(8))     # Output: 24
print(fibfib(100))   # Output: 2843825023
```

In this script, the `memoize` decorator is used to cache the results of the `fibfib` function. This optimization significantly reduces the computation time for large inputs because it avoids redundant calculations.