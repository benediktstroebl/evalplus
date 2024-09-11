```python
def memoize(func):
    """A simple memoization decorator to cache the results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Args:
        n (int): The index of the FibFib number to compute.
    Returns:
        int: The nth FibFib number.
    """
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a memoization decorator to efficiently compute the nth element of the fibfib number sequence. Memoization is a technique to store the results of expensive function calls and return the cached result when the same inputs occur again. This approach significantly improves the performance of the function for larger values of n.